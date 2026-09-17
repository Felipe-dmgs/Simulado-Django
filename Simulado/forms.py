from django import forms
from .models import Livro, Acervo

class LivroForm(forms.ModelForm):
    class Meta():
        model = Livro
        fields = ['titulo','autor','ano']

class AcervoForm(forms.ModelForm):
    class Meta():
        model = Acervo
        fields = ['tipo', 'categoria']