from django.urls import path
from .views import index, contact, events, brewery, reservation, gallery

urlpatterns = [
    path('', index, name='index'),
    path("contact/", contact, name="contact"),
    path("events/", events, name='events'),
    path("brewery/", brewery, name='brewery'),
    path("reservation/", reservation, name='reservation'),
    path("gallery/", gallery, name='gallery'),
]