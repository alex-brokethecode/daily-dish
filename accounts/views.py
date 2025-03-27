from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def login_view(request):
    return render(request=request, template_name='accounts/login.html')


@login_required(login_url='accounts:login')
def logout_view(request):
    logout(request)
    return redirect('menu:home')
