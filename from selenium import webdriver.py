from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Defina o caminho para o seu chromedriver
path_to_chromedriver = "C:/caminho/para/o/chromedriver.exe"  # Atualize para o caminho correto

# Configurações do Chrome
chrome_options = Options()
chrome_options.add_argument("--lang=pt-BR")  # Configura o idioma para português (Brasil)

# Inicia o serviço do WebDriver e passa o caminho do chromedriver
service = Service(path_to_chromedriver)

# Criação do WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Acessar o site
driver.get("https://www.casasbahia.com")

# Espera para o site carregar
time.sleep(3)

# Enviar uma busca de exemplo
search_box = driver.find_element_by_xpath("//input[@placeholder='O que você está procurando?']")
search_box.send_keys("geladeira")
search_box.send_keys(Keys.RETURN)

# Aguarde os resultados
time.sleep(3)

# Imprimir o título do primeiro produto encontrado
first_product = driver.find_element_by_xpath("//h2[@class='product-title']")
print("Primeiro produto:", first_product.text)

# Fechar o navegador
driver.quit()
