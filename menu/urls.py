from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('produk/', views.produk, name='produk'),
    path('produk/detail/<int:id>', views.detail_produk, name='detail_produk'),
    path('dt/', views.dt, name='dt'),
]