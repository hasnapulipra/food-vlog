from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns=[
    path('cartdetails',views.cartdetails,name='cartdetails'),
    path('add/<int:product_id>/',views.add_cart,name='add_cart'),
    path('min_cart/<int:product_id>/', views.min_cart, name='min_cart'),
    path('cart_delete/<int:product_id>/', views.cart_delete, name='cart_delete')
]