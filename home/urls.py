from django.contrib import admin
from . import views 
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vuelos.urls')), 
    path('registrar/', views.registrar_vuelos, name='registrar_vuelos'),
    path('listar/', views.listar_vuelos, name='listar_vuelos'),
    path('estadisticas/', views.estadisticas_vuelos, name='estadisticas_vuelos'),
]