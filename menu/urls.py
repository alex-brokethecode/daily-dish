from django.urls import path

from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.dish_list, name='dish_list'),
    path('menu/platillo/<int:pk>', views.dish_detail, name='dish_detail')
]
