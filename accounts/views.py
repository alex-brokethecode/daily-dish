from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from manager.models import BusinessInfo
from .forms import LoginForm


def login_view(request):
    next_url = request.GET.get('next', 'menu:home')

    if request.user.is_authenticated:
        return redirect(next_url)

    form = LoginForm(request, data=request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.get_user()

        if user is not None:
            login(request, user)
            messages.success(request, 'Ha iniciado sesión correctamente')
            return redirect(next_url)
        else:
            form.add_error(None, 'Usuario o contraseña incorrecta')

    context = {
        'business_name': BusinessInfo.objects.first().name,  # type: ignore
        'form': form,
    }

    return render(request=request, template_name='accounts/login.html', context=context)


@login_required(login_url='accounts:login')
def logout_view(request):
    logout(request)
    messages.success(request, 'Ha cerrado sesión correctamente')
    return redirect('menu:home')
