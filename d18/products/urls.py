from django.urls import path

from .views import *

app_name = 'products'

urlpatterns = [
    path('', products, name = 'index'),
    path('category/<int:category_id>/', products, name = 'category'),
    path('baskets/add/<int:product_id>/', basket_add, name = 'basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name = 'basket_remove')
]


