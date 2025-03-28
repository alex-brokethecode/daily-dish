from django.shortcuts import render, redirect
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import BusinessInfo
from menu.models import Menu, MenuItem


@login_required(login_url='accounts:login')
def manager(request):
    today = now().date()
    menu = Menu.objects.filter(date=today).first()

    context = {
        'business_name': BusinessInfo.objects.first().name,  # type: ignore
        'menu': menu,
    }
    return render(request=request, template_name='manager/manager.html', context=context)


@login_required(login_url='accounts:login')
def update_sold_dishes(request, pk):
    menu_item = MenuItem.objects.get(id=pk)

    if request.method == 'POST':
        sold_dishes = request.POST.get('sold')

        try:
            sold_dishes = int(sold_dishes)
        except ValueError:
            messages.error(request, 'Cantidad no válida')
            return redirect('manager:sales')

        if sold_dishes > menu_item.remaining_stock():
            messages.error(request, 'No hay suficiente stock')
            return redirect('manager:sales')

        menu_item.sold = menu_item.sold + sold_dishes
        menu_item.save()

        messages.success(request, 'Cantidad actualizada correctamente')
    return redirect('manager:sales')
