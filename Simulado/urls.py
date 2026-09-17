from django.urls import path
from . import views

urlpatterns = [
    path('livros/', views.list_livros, name='lista'),
    path('buscar/', views.encontrar_livro, name='encontrar_livro'),
    path('novo/', views.novo_livro, name='novo_livro'),
]