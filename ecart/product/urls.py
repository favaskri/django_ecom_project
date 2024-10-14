
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('product_lists/',views.product_lists,name='product_lists'),
    path('product_detail/',views.product_detail,name='product_detail')
]
