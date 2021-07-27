from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from .forms import ContactUsForm
from .models import AboutUs


class CreateContactUsObject(CreateView):
    form_class = ContactUsForm
    success_url = '/'
    template_name = 'contact/contact_us.html'


def about_us(request):
    post = AboutUs.objects.first()
    return render(request, 'contact/about_us.html', {'post': post})
