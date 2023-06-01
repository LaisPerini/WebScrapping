# Importando Libs
from requests import get
from bs4 import BeautifulSoup
from warnings import warn
from time import sleep
from random import randint
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import seaborn as sns

paginas = np.arange(1, 5, 50)
headers = {'Accept-Language': 'pt-BR,pt;q=0.8'}

titulos = [] 
anos = []
generos = []
tempo_duracao = []
votos = []

ratings = []
imdb_ratings = []


for pagina in paginas:

    response = get("https://www.imdb.com/search/title?genres=sci-fi&"
    + "start=" + str(pagina) + "&explore=title_type,genres&ref_=adv_prv", headers=headers)

    sleep(randint(8, 16))
    if response.status_code != 200:
        warn(f'O pedido: {requests} retornou o código: {response.status_code}') 
    
    # Pegando informações das páginas
    pagina_html = BeautifulSoup(response.text, 'html.parser')

    # Pegando informações por containers
    movie_containers = pagina_html.find_all('div', class_ = 'lister-item mode-advanced')

    for container in movie_containers:
        
        # capturando titulos
        if container.find('div', class_ = 'ratings-metascore') is not None:
            title = container.h3.a.text
            titulos.append(title)

            # Capturando anos
            if container.h3.find('span', class_ = 'lister-item-year text-muted unbold') is not None:
                year = container.h3.find('span', class_ = 'lister-item-year text-muted unbold').text
                anos.append(year)
            else:
                anos.append(None)

            # Capturando avaliação
            if container.p.find('span', class_ = 'certificate') is not None:
                avaliacao = container.p.find('span', class_ = 'certificate').text
                ratings.append(avaliacao)
            else:
                ratings.append(None)

            # Capturando Gênero
            if container.p.find('span', class_ = 'genre') is not None:
                genero = container.p.find('span', class_ = 'genre').text.replace('\n', '').strip().split(',')
                generos.append(genero)
            else:
                generos.append(None)

             # Capturando duração dos filmes
            if container.p.find('span', class_ = 'runtime') is not None:
                tempo = int(container.p.find('span', class_ = 'runtime').text.replace('min', ''))
                tempo_duracao.append(tempo)
            else:
                tempo_duracao.append(None)

            # Capturando votos IMDB  6.8
            if container.strong.text is not None:
                imdb = float(container.strong.text.replace(',', '.'))
                imdb_ratings.append(imdb)
            else:
                imdb_ratings.append(None)

            # Capturando votos
            if container.find('span', attrs = {'name':'nv'})['data-value'] is not None:
                voto = int(container.find('span', attrs = {'name':'nv'})['data-value'])
                votos.append(voto)
            else:
                votos.append(None)

dt_inicial = pd.DataFrame({
    'ano': anos,
    'genero': generos,
    'tempo': tempo_duracao,
    'imdb': imdb_ratings,
    'votos': votos
})

dt_inicial.loc[:, 'ano'] = dt_inicial['ano'].str[-5:-1] 
dt_inicial['imdb_conv'] = dt_inicial['imdb'] * 10

dt_final = dt_inicial.loc[dt_inicial['ano'] != 'Movie']

print(dt_final)