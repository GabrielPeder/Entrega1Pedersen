from django.urls import path
from Providers.views import providers_list, providers_create, provider_update, ProviderDeleteView

urlpatterns = [
    path('providers_list/', providers_list, name='providers_list'),
    path('provider_add/', providers_create, name='provider_add'),
    path('provider_update/<int:pk>/', provider_update, name='provider_update'),
    path('provider_delete/<int:pk>/', ProviderDeleteView.as_view(), name='provider_delete'),

]