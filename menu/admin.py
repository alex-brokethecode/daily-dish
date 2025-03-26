from django.contrib import admin
from .models import Dish, Menu, MenuItem


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created',)
    search_fields = ('name', 'description',)
    list_filter = ('created', 'updated', 'price',)


class MenuItemInline(admin.TabularInline):  # Inline to embed inside MenuAdmin
    model = MenuItem
    extra = 1  # Number of empty forms to show by default
    autocomplete_fields = ('dish',)  # Enables search for dishes
    fields = ('dish', 'stock', 'sold')  # Only show necessary fields


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('date', 'created', 'updated',)
    search_fields = ('date',)
    list_filter = ('date',)
    inlines = (MenuItemInline, )  # Attach the MenuItem inline to Menu
