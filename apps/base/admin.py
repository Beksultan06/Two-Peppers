from django.contrib import admin
from apps.base.models import ContactSettings, Pages, Images, ContactMessage, Reservation, ContactPage, \
Events, EventsOBJ, About, Sheff, Testimonials, ReservationSettings, SettingsMainPages, ImageBanner,\
MenuItem, MenuCategory, Gallery

class ImagesInline(admin.TabularInline):
    model = Images
    extra = 1

@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
    inlines = [ImagesInline]

admin.site.register(ContactSettings)
admin.site.register(ContactPage)
admin.site.register(Events)
admin.site.register(EventsOBJ)
admin.site.register(About)
admin.site.register(Sheff)
admin.site.register(Testimonials)
admin.site.register(Reservation)
admin.site.register(ReservationSettings)
admin.site.register(SettingsMainPages)
admin.site.register(ImageBanner)
admin.site.register(Gallery)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("created_at","name","email","telegram_ok")
    search_fields = ("name","email","message")
    list_filter = ("telegram_ok", "created_at")

class MenuItemAdmin(admin.TabularInline):
    model = MenuItem
    extra = 1

@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    inlines = [MenuItemAdmin]