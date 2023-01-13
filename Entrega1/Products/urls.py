
from django.urls import path
from Products import views
from Products.views import add_product, list_products,searchform


urlpatterns = [
    path('add_product/', add_product),
    path('list_products/', list_products),
    path('search/', searchform),
]