from django.shortcuts import render, redirect
from .models import Livro, Acervo
from .forms import LivroForm, AcervoForm

def list_livros(request):
    livros = Livro.objects.all()
    return render(request, 'lista.html', {'livros': livros})


def novo_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        acervo_form = AcervoForm(request.POST)
        if form.is_valid() and acervo_form.is_valid():
            livro = form.save()
            acervo = acervo_form.save()
            acervo.livro.add(livro)
            return redirect('lista')
    else:
        form = LivroForm()
        acervo_form = AcervoForm()
    return render(request, 'forms.html', {'form': form, 'acervo_form': acervo_form})

def encontrar_livro(request):
    nome = request.GET.get("nome", "").strip()
    tipo = request.GET.get("tipo", "").strip()
    categoria = request.GET.get("categoria", "").strip()

    if not nome and not tipo and not categoria:
        return redirect('lista')

    acervos = Acervo.objects.all().prefetch_related("livro")
    
    if nome:
        acervos = acervos.filter(livro__titulo__icontains=nome)
        
    if tipo:
        acervos = acervos.filter(tipo=tipo)
        
    if categoria:
        acervos = acervos.filter(categoria=categoria)
        
    acervos = acervos.distinct()
    
    context = {
        "acervos": acervos,
        "tipos": Acervo.Type.choices,          
        "categorias": Acervo.Category.choices,  
        
        "nome": nome,
        "tipo": tipo,
        "categoria": categoria,
    }
    
    return render(request, 'lista.html', context)