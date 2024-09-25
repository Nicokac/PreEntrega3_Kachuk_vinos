from django.urls import path
from . import views

urlpatterns = [
    path('preferencias/', views.agregar_preferencia, name='agregar_preferencia'),
    path('recomendaciones/', views.recomendar_vinos, name='recomendar_vinos'),
    path('', views.index, name='index'),
]
