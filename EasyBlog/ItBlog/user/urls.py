from django.urls import path

from user.views import Logout, register, Login

urlpatterns = [

    path('register/', register, name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout')
]
