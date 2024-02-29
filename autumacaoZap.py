# Importando bibliotecas para automação no WhatsApp
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.parse
import time

# Mensagem 
MESSAGE_SENT = (
    "Cliente assinante, Temos ótimas notícias para você! Excepcionalmente neste mês, vamos aumentar a "
    "frequência de envio dos produtos de sua assinatura para um total de 5 vezes. Estamos empolgados em "
    "oferecer a você ainda mais do que ama, diretamente na sua porta, sem custo adicional. Fique atento(a) "
    "às datas de entrega e prepare-se para desfrutar ainda mais dos nossos produtos selecionados "
    "especialmente para você."
)

# Carregando números de telefone a partir de um arquivo Excel
numbers_df = pd.read_excel("E:\\Python\\Klauber\\venv\\contatos.xlsx")
print(numbers_df)

# Inicializando o navegador Chrome
browser = webdriver.Chrome()
browser.get("https://web.whatsapp.com")

# Espera até que o QR Code seja escaneado
wait = WebDriverWait(browser, 30)  #Tempo de espera para dar mais tempo de escanear o QR Code


# Enviando mensagens
for i, nome in numbers_df.iterrows():
    number = nome["NUMERO"]
    text = urllib.parse.quote(MESSAGE_SENT)
    link = f"https://web.whatsapp.com/send?phone={number}&text={text}"
    browser.get(link)
    wait = WebDriverWait(browser, 60)
    input_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p')))
    input_field.send_keys(Keys.ENTER)
    time.sleep(10)  # Pausa entre o envio de mensagens para evitar bloqueios ou comportamento indesejado
