from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now

from .models import Dish, Menu, MenuItem


def home(request):
    return render(request=request, template_name='menu/home.html')


def dish_list(request):
    today = now().date()
    menu = Menu.objects.filter(date=today).first()

    context = {'menu': menu}

    return render(request=request, template_name='menu/dish_list.html', context=context)


def dish_detail(request, pk):
    dish = get_object_or_404(Dish, id=pk)

    # Get today's menu (if it exists)
    today = now().date()
    menu = Menu.objects.filter(date=today).first()  # Get today's menu

    # Get the stock of this dish for today's menu (if available)
    stock = None
    if menu:
        menu_item = MenuItem.objects.filter(menu=menu, dish=dish).first()
        if menu_item:
            stock = menu_item.remaining_stock

    context = {'dish': dish, 'stock': stock}

    return render(request=request, template_name='menu/dish_detail.html', context=context)
