from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('buku/detail/<int:id>', views.detail_buku, name='detail_buku'),
    path('dt/', views.dt, name='dt'),
    path('book/', views.book, name='book'),
    path('list/', views.list, name='list'),
]