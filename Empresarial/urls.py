from django.urls import path
from .import views
urlpatterns= [
    path('', views.home),
    path('registrarempresa/', views.registrarempresa),
    path('eliminarempresa/<nit>', views.eliminarempresa)
]