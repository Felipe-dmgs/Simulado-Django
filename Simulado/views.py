from django.shortcuts import render
from .models import Livro, Acervo
from .forms import LivroForm

def list_livros(request):
    livros = Livro.objects.all()
    return render(request, 'acervo/lista.html', {'livros': livros})


def novo_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = LivroForm()
    return render(request, 'Simulado/form.html', {'form': form})

def encontrar_livro(request):
    nome = request.GET.get("nome", "").strip()
    tipo = request.GET.get("tipo", "").strip()
    categoria = request.GET.get("categoria", "").strip()
    
    acervos = Acervo.objects.all().prefetch.related("livro")
    
    if nome:
        acervos = acervos.filter(
            livro__titulo__icontains = nome
        )
    if tipo:
        acervos = acervos.filter(
            acervos = acervos.filter(tipo=tipo)
        )
    if categoria:
        acervos = acervos.filter(categoria=categoria)
        
    acervos = acervos.distinct()
    
    context = {
        "acervos" = acervos,
        "tipos" = Acervo.tipo.choices,
        "categorias" = Acervo.categoria.choices,
        
        "nome": nome,
        "tipo": tipo,
        "categoria": categoria,
    }