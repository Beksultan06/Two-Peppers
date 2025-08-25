from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .forms import ContactForm
from .utils import send_telegram_message
from apps.base.models import ContactSettings, ContactMessage, ContactPage, Events, EventsOBJ, \
About, Sheff, Testimonials, Reservation, ReservationSettings, SettingsMainPages, \
ImageBanner, MenuCategory, Gallery
    
def events(request):
    events_id = Events.objects.latest("id")
    events_all = EventsOBJ.objects.all()
    return render(request, "events-list.html", locals())

def index(request):
    settings_id = SettingsMainPages.objects.latest("id")
    image_all  = ImageBanner.objects.all()
    categories = MenuCategory.objects.prefetch_related('items').all()
    testimonials = Testimonials.objects.all()
    about_id = About.objects.latest("id")
    gallery_all = Gallery.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        Testimonials.objects.create(
            name=name,
            email=email,
            text=message
        )
        return redirect('index')  
    return  render (request, 'index2.html', locals())
    
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

def brewery(request):
    about_id = About.objects.latest("id")
    sheff_all = Sheff.objects.all()
    testimonials_all = Testimonials.objects.all()
    return render(request, 'our-brewery.html', locals())

def reservation(request):
    reservation_all = Reservation.objects.all()
    reservation_id = ReservationSettings.objects.latest("id")
    return render(request, "reservation.html", locals())