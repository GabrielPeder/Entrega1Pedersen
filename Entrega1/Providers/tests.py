from django.urls import path
from Providers.views import providers_list, providers_create, provider_update, ProvidersListView, \
    ProviderCreateView, ProviderDeleteView

urlpatterns = [
    path('providers_list/', ProvidersListView.as_view(), name='providers_list'),
    path('provider_create/', ProviderCreateView.as_view(), name='providers_create'),
    path('provider_update/<int:pk>/', provider_update, name='provider_update'),
    path('provider_delete/<int:pk>/', ProviderDeleteView.as_view(), name='provider_delete'),

]