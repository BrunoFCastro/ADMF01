import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

service = Service()
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service, options=options)

url = 'https://maitredigital.com.br/salvadorrestaurantweek'

driver.set_page_load_timeout(3000000)
driver.implicitly_wait(3000000)

driver.get(url)

expand = True
while(expand):
    try:
        driver.find_element(By.CLASS_NAME,"EventContainer__pagination").click()
    except:
        expand = False

restaurantes = driver.find_elements(By.CLASS_NAME, "Title ")
cozinhas = driver.find_elements(By.CLASS_NAME, "EventRegistrationCardText__cuisines")
enderecos = driver.find_elements(By.CLASS_NAME, "EventRegistrationCardText__address")
valores = driver.find_elements(By.CLASS_NAME, "EventRegistrationCardText__periods")

lista = []
item = 0
restaurantes = restaurantes[11:len(restaurantes)]

for i in range(len(restaurantes)):
    lista.append(
        '"Nome":' + restaurantes[i].text + 
        ', "Cozinha":' + cozinhas[i].text +
        ', "Endereco":' + enderecos[i].text +
        ', "Valor":' + valores[i].text
        )

with open("dados.txt", "w", encoding="utf-8") as arquivo:
    for linha in lista:
        arquivo.write(linha+"\n")

driver.close()