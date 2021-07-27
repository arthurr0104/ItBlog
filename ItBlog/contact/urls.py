from django.urls import path

from .views import CreateContactUsObject, about_us

urlpatterns = [
    path('contact_us/', CreateContactUsObject.as_view(), name='contact_us'),
    path('about_us/', about_us, name='about_us'),
]
