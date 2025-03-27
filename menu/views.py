from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now

from .models import Dish, Menu, MenuItem
from manager.models import BusinessInfo


def home(request):
    context = {'business': BusinessInfo.objects.first()}
    return render(request=request, template_name='menu/home.html', context=context)


def dish_list(request):
    today = now().date()
    menu = Menu.objects.filter(date=today).first()
    business = BusinessInfo.objects.first()

    context = {'menu': menu, 'business': business}

    return render(request=request, template_name='menu/dish_list.html', context=context)


def dish_detail(request, pk):
    dish = get_object_or_404(Dish, id=pk)
    business = BusinessInfo.objects.first()

    # Get today's menu (if it exists)
    today = now().date()
    menu = Menu.objects.filter(date=today).first()  # Get today's menu

    # Get the stock of this dish for today's menu (if available)
    stock = None
    if menu:
        menu_item = MenuItem.objects.filter(menu=menu, dish=dish).first()
        if menu_item:
            stock = menu_item.remaining_stock

    context = {'dish': dish, 'stock': stock, 'business': business}

    return render(request=request, template_name='menu/dish_detail.html', context=context)
