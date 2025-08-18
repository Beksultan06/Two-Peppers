from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .forms import ContactForm
from .utils import send_telegram_message
from apps.base.models import ContactSettings, ContactMessage, ContactPage

def index(request):
    return render (request, 'index2.html')
    
def contact(request):
    obj_all = ContactSettings.objects.all()
    contact_id = ContactPage.objects.latest("id")
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cm = ContactMessage.objects.create(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                message=form.cleaned_data["message"],
                ip=request.META.get("REMOTE_ADDR"),
                user_agent=request.META.get("HTTP_USER_AGENT", ""),
            )
            ok, err, msg_id = send_telegram_message(
                form.cleaned_data["name"],
                form.cleaned_data["email"],
                form.cleaned_data["message"]
            )
            cm.telegram_ok = ok
            cm.telegram_error = "" if ok else (str(err)[:1000]) 
            cm.telegram_message_id = msg_id
            cm.save(update_fields=["telegram_ok","telegram_error","telegram_message_id"])
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                if ok:
                    return JsonResponse({"ok": True, "message": "Спасибо! Сообщение отправлено."})
                else:
                    return JsonResponse(
                        {"ok": False, "error": "Не удалось отправить сообщение в Telegram.", "details": cm.telegram_error},
                        status=502
                    )
            else:
                if ok:
                    messages.success(request, "Спасибо! Сообщение отправлено.")
                else:
                    messages.error(request, "Не удалось отправить сообщение в Telegram. Мы сохранили вашу заявку и свяжемся позже.")
                return redirect("contact")
        else:
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"ok": False, "errors": form.errors}, status=400)
    else:
        form = ContactForm()
    return render(request, "contact-us.html", locals())