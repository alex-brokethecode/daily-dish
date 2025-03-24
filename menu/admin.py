from django.contrib import admin
from .models import Dish


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'created',)
    search_fields = ('name', 'description',)
    list_filter = ('created', 'updated', 'price', 'quantity')
