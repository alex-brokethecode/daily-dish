from django.urls import path

from . import views

app_name = 'manager'

urlpatterns = [
    path('', views.manager, name='sales'),
    path('update-sold-dishes/<int:pk>/',
         views.update_sold_dishes, name='update_sold_dishes'),
]
