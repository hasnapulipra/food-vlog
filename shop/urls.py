from django.contrib import admin

from django.urls import path
from . import views
urlpatterns = [

    path('',views.home,name='home'),
    path('<slug:c_slug>/',views.home,name='prod_cat'),
   path('<slug:c_slug>/<slug:product_slug>',views.proddetail,name='proddetail'),
    path('search',views.search,name='search')
]