from django.shortcuts import render, get_object_or_404

from .models import Dish


def home(request):
    return render(request=request, template_name='menu/home.html')


def dish_list(request):
    dishes = Dish.objects.all()
    context = {'dishes': dishes}
    return render(request=request, template_name='menu/dish_list.html', context=context)


def dish_detail(request, pk):
    dish = get_object_or_404(Dish, id=pk)
    context = {'dish': dish}

    return render(request=request, template_name='menu/dish_detail.html', context=context)
