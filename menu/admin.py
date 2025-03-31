from django.contrib import admin
from .models import Dish, Menu, MenuItem


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created',)
    search_fields = ('name', 'description',)
    list_filter = ('created', 'updated', 'price',)
    readonly_fields = ('created', 'updated',)


class MenuItemInline(admin.TabularInline):  # Inline to embed inside MenuAdmin
    model = MenuItem
    extra = 10  # Number of empty forms to show by default
    autocomplete_fields = ('dish',)  # Enables search for dishes
    # Only show necessary fields
    fields = ('dish', 'stock', 'sold', 'price_at_sale')


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('date', 'created', 'updated',)
    search_fields = ('date',)
    list_filter = ('date',)
    inlines = (MenuItemInline, )  # Attach the MenuItem inline to Menu
