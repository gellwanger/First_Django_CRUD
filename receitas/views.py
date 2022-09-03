from django.shortcuts import render

def index(request):
  receitas = {
    1: 'Aligot de batata',
    2: 'Macarons au chocolat',
    3: 'Pain au chocolat',
    4: 'File au poivre',
    5: 'Pain perdu',
    6: 'Petit gâteau',
  }

  dados = {
    'nome_das_receitas' : receitas,
  }

  return render(request, 'index.html', dados)

def receita(request):
  return render(request, 'receita.html')
