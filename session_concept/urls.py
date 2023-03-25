from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('load/',views.load_products),
    path('product/<int:product_id>/',views.product,name='product')
]
