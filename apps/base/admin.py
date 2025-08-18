from django.contrib import admin
from apps.base.models import ContactSettings, Pages, Images, ContactMessage, ContactPage

class ImagesInline(admin.TabularInline):
    model = Images
    extra = 1

@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
    inlines = [ImagesInline]

admin.site.register(ContactSettings)
admin.site.register(ContactPage)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("created_at","name","email","telegram_ok")
    search_fields = ("name","email","message")
    list_filter = ("telegram_ok", "created_at")