# Importando as bibliotecas necessárias
from django.shortcuts import render
from datetime import date
from .models import Tweet, Article, Reference
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def home(request):
  return render(request, 'portal/home.html')

def articles(request):
  articles = Article.objects.all()
  return render(request, 'portal/articles.html')

def portals(request):
  references = Reference.objects.all()
  return render(request, 'portal/portals.html')

def tweets_search(request):
  return render(request, 'portal/tweets_search.html')

def graphics(request):
  if request.method == 'POST':
    data = []
    attributes = []
    # Recebe os dados
    data_group = request.POST.get('data').split('\n')

    # Obtém os atributos das colunas
    attributes = data_group[0].split(',')
    attributes[len(attributes)-1] = attributes[len(attributes)-1][:-1]

    # Evita que o usuário não escreva atributos
    if attributes == ['']:
      return render(request, 'portal/graphics.html')

    # Armazena em data os dados das colunas
    for i, line in enumerate(data_group):
      if i != 0:
        if i + 1 != len(data_group):
          data.append(line[:-1].split(','))
        else:
          data.append(line.split(','))
        
        # Evita que o usuário preencha os dados de forma errada
        try:
          data[i-1] = list(map(float, data[i-1]))
        except:
          return render(request, 'portal/graphics.html')

    # Evita que o usuário preencha os dados de forma errada
    if not all(len(attributes)== len(i) for i in data) or len(data) == 0:
      return render(request, 'portal/graphics.html')

    chart = request.POST.get('graphic')
    # Cria uma figura do matplotlib
    fig = plt.figure()

    # Checa o tipo do gráfico pedido
    if chart == 'pie':
      # Transforma os dados em um array de numpy os somando
      data = sum(map(np.array, data))
      # Cria um dataframe de pandas a partir do array
      df = pd.DataFrame(data)
      # Plota o gráfico a partir do dataframe
      plt.pie(data, labels=attributes, autopct='%1.1f%%')

    elif chart == 'line':
      # Armazena em um dataframe o array feito com os dados
      df = pd.DataFrame(np.array(data), columns=attributes)
      # Plota o gráfico
      plt.plot(df)
      # Define a legenda do gráfico (os atributos)
      plt.legend(df.columns)

    else:
      # Cria o dataframe a partir dos dados, com colunas e índices definidos
      df = pd.DataFrame(np.array(data), columns=attributes, index=np.arange(0, len(data)))
      # Plota o gráfico do tipo barra ou área
      fig = df.plot(kind = chart).get_figure()

    # Salva a figura gerada como graph.jpg
    fig.savefig('portal/static/graph.jpg')

    return render(request, 'portal/graphics_result.html')
  
  else:
    return render(request, 'portal/graphics.html')