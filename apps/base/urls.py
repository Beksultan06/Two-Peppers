from django.urls import path
from .views import index, contact, events, brewery

urlpatterns = [
    path('', index, name='index'),
    path("contact/", contact, name="contact"),
    path("events/", events, name='events'),
    path("brewery/", brewery, name='brewery')
]
