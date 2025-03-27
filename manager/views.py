from django.shortcuts import render
from django.utils.timezone import now

from .models import BusinessInfo
from menu.models import Menu


def manager(request):
    today = now().date()
    menu = Menu.objects.filter(date=today).first()

    context = {
        'business_name': BusinessInfo.objects.first().name,  # type: ignore
        'menu': menu,
    }
    return render(request=request, template_name='manager/manager.html', context=context)
