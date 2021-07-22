from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User, UserManager
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render, redirect

from user.forms import CustomUserCreationForm, MyUserLoginForm

from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Պրոֆիլը հաջողությամբ ստեղծվել է!')
            return redirect('home')
        else:
            messages.error(request, 'Պրոֆիլի ստեղծումը ավարտվեց անհաջողությամբ!')
    else:

        form = CustomUserCreationForm()
    return render(request, 'user/register.html', {'form': form})


class Login(LoginView):
    template_name = 'user/login.html'
    authentication_form = MyUserLoginForm


class Logout(LogoutView):
    pass
