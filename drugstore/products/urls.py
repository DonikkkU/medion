from django.urls import path
from .views import *



urlpatterns = [
    path('products/', products, name='products'),
    path('products/<uuid:id>', product, name='product'),
    path('', main, name='main')
]