from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views


def home(request):
    return render(request, 'profile/home.html')

def logout(request):
    request.session.flush()
    return redirect('/user/')

class LoginView(auth_views.LoginView):
    template_name = 'profile/login.html'