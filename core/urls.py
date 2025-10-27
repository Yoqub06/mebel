from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('product/', views.product, name='product'),
    path('contacts/', views.contacts, name='contacts'),
    path('compare/', views.compare, name='compare'),
    path('catalog/', views.catalog, name='catalog'),
    path('cart/', views.cart, name='cart'),
]
