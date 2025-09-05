from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
# Create your views here.
class LoginUser(LoginView):
    template_name               = 'authenticate/login.html'
    # redirect_authenticated_user = reverse_lazy('dashboard:dashboard')
