from django.urls import path
from . import views

urlpatterns = [
    path(
        'livros/',
        views.lista_livros,
        name='lista'
    ),
    path(
        'buscar/', 
        views.buscar_produtos, 
        name='buscar_produtos'
    ),
]