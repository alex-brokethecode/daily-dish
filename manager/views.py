from django.shortcuts import render
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required

from .models import BusinessInfo
from menu.models import Menu


@login_required(login_url='accounts:login')
def manager(request):
    today = now().date()
    menu = Menu.objects.filter(date=today).first()

    context = {
        'business_name': BusinessInfo.objects.first().name,  # type: ignore
        'menu': menu,
    }
    return render(request=request, template_name='manager/manager.html', context=context)
