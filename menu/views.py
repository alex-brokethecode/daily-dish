from django.shortcuts import render

from .models import Dish


def dish_list(request):
    dishes = Dish.objects.all()

    return render(request, 'menu/dish_list.html', {'dishes': dishes})
