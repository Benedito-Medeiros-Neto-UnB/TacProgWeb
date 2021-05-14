# Importando as bibliotecas necessárias
from django.shortcuts import render
import snscrape.modules.twitter as sntwitter
from datetime import date
from .models import Tweet, Article, Reference
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import requests


def tweets_list(request):
  return render(request, 'portal/tweets_list.html', {'tweets': ['Realize uma busca para verificar os resultados!']})

def home(request):
  return render(request, 'portal/home.html')

def articles(request):
  articles = Article.objects.all()
  return render(request, 'portal/articles.html', {'articles': articles})

def portals(request):
  references = Reference.objects.all()
  return render(request, 'portal/portals.html', {'references': references})

def tweets_search(request):
  if request.method == 'POST':
    key_groups = []
    # Recebo os dados enviados pelo usuário
    username = request.POST.get('username')
    start_date = request.POST.get('startDate').split('-')
    end_date = request.POST.get('endDate').split('-')
    type_search = request.POST.get('search')
    num_search = request.POST.get('num')
    keywords = request.POST.get('words').split(',')

    # Evita que usuários deixem de preencher algo
    if keywords == [''] or start_date == [''] or end_date == ['']:
      return render(request, 'portal/tweets_search.html')

    # Adapto a data no formato DD-MM-AAAA para AAAA-MM-DD
    begin_date = f'{start_date[2]}-{start_date[1]}-{start_date[0]}'
    end_date = f'{end_date[2]}-{end_date[1]}-{end_date[0]}'

    num = len(keywords)
    j = 0
    # Crio a string que determina a raspagem a ser feita
    search = ''
    while num > j:
      # Caso tenha usuário, defino que deve ser concatenado seu username
      if username != '' and j == 0:
        search = search + f'from:{username}'
      # Concateno a primeira keyword
      if j == 0:
        search = search + f' {keywords[0]}'
      # Concateno as demais keywords
      else:
        # Concateno com AND caso deseje tweets com todos as keywords
        if type_search == 'all-kw':
          search = search + f' AND {keywords[j]}'
        # Concateno com OR caso deseje tweets com no mínimo uma keyword
        else:
          search = search + f' OR {keywords[j]}'
      j += 1

    # Concateno as datas de início e fim da busca
    search = search+ f' since:{begin_date}' + f' until:{end_date}'

    tweets = []
    datas = []
    # Realiza a busca definida anteriormente, se limitando com o número máximo de tweets
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(search).get_items()):
      if num_search != 'ilimitado' and i > int(num_search):
        break
      
      # Recebe e formata a data do tweet
      data = str(tweet.date).split()[0]
      data = data.split('-')
      data = f'{data[2]}-{data[1]}-{data[0]}'
      tweets.append([data, tweet.content])

    return render(request, 'portal/tweets_list.html', {'tweets': tweets})
  else:
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
          data[i-1] = list(map(int, data[i-1]))
        except:
          return render(request, 'portal/graphics.html')

    # Evita que o usuário preencha os dados de forma errada
    if not all(len(attributes)== len(i) for i in data) or len(data) == 0:
      return render(request, 'portalgraphics.html')

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

def query_constructor(exact_match = [], partial_match = []):
  query = ''
  for i in range(0, len(exact_match)):
    if (i != len(exact_match) - 1):
      query += '"' + exact_match[i] + '" OR '
    else:
      query += '"' + exact_match[i] + '" '

  if len(partial_match) > 0:
    query += 'OR '

  for i in range(0, len(partial_match)):
    query += '('
    for j in range(0, len(partial_match[i])):
      if (j != len(partial_match[i]) - 1):
        query += '"' + partial_match[i][j] + '" AND '
      else:
        query += '"' + partial_match[i][j] + '"'
    if (i != len(partial_match) - 1):
      query += ') OR '
    else:
      query += ') '

  return query/
