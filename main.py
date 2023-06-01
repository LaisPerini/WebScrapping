# importando Libs
from requests import get
from bs4 import BeautifulSoup
from warnings import warn
from time import sleep
from random import randint
import matplotlib.pyplot as plt
import pandas as pd
import requests
import numpy as np
import seaborn as sns


paginas = np.arange(1,5,50)      # criando um array
headers = {'Accept-Language' : 'pt-BR,pt;q=0.8'} 

titulo = []
anos  =[]                  
generos =[]
tempo_duracao =[]
votos =[]
ratings =[]
imdb_rating =[]
imdb_ratings_standardized =[]

for pagina in paginas :
    
    response = get("https://www.imdb.com/search/title?genres=sci-fi&" 
    + "start=" + str(pagina) + "&explore=title_type,genres&ref_=adv_prv", headers=headers)      
    #print(response)
    sleep(randint(8,16))                                   #sleep = pausa de segundos  entre 8 e 16 segundos no caso
    if response.status_code != 200:
        warn(f'O pedido:{requests} retornou o codigo: {response.status_code}')

 # pegando informações das paginas 
    pagina_html = BeautifulSoup(response.text,'html.parser')
     #print(pagina_html)

 #pegando informações por containers
    movie_containers = pagina_html.find_all('div',class_ = 'lister-item mode-advanced')     # procurando uma div que a class é = lister..etc    

print(movie_containers)






# request               #request pedindo a informacao , reponse 

 #request pedindo a informacao , reponse 
