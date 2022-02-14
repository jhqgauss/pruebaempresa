from django.urls import path
from .import views
urlpatterns= [
    path('', views.home),
    path('registrarempresa/', views.registrarempresa),
    path('edicionempresa/<nit>', views.edicionempresa),
    path('edicionempresa/editarempresa/', views.editarempresa),
    path('eliminarempresa/<nit>', views.eliminarempresa)
   
    
]