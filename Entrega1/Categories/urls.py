from django.urls import path
from Categories.views import list_categories, add_category   


urlpatterns = [
    path('add_categories/', add_category),
    path('list_categories/', list_categories)

]