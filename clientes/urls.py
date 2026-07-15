from django.urls import path,include
from clientes import views

urlpatterns = [
    path('clientes/', views.clientes_view, name= 'cliente')
]