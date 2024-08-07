# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 21:39:59 2024

@author: danim
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Definir lURL del objetivo de scraping
url = 'https://www.scrapethissite.com/pages/simple/'

# Hacer la solicitud GET a la página web
response = requests.get(url)

# Parsear el contenido HTML con BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extraer los datos deseados
data = []
for row in soup.find_all('div', class_='team'):
    name = row.find('h3').text.strip()
    year = row.find('span', class_='year').text.strip()
    wins = row.find('span', class_='wins').text.strip()
    losses = row.find('span', class_='losses').text.strip()
    data.append([name, year, wins, losses])
    
   # Crear un DataFrame con los datos extraídos
df = pd.DataFrame(data, columns=['Team', 'Year', 'Wins', 'Losses']) 

# Guardar los datos en un archivo CSV
df.to_csv('scraped_data.csv', index=False)

print("Datos extraídos y guardados en 'scraped_data.csv'")
