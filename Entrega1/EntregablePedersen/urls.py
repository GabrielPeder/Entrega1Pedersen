from django.contrib import admin
from django.urls import path, include
from EntregablePedersen.views import index

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),

    path('Products/', include('Products.urls')),
    path('Categories/', include('Categories.urls')),
    path('Providers/', include('Providers.urls')),

]
