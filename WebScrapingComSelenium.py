from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Configuração do ChromeDriver
options = Options()
# options.add_argument("--headless")  # Executa sem abrir janela
options.add_argument("--no-sandbox")

# Aponta para o chromedriver na raiz do projeto
service = Service(executable_path="./chromedriver-linux64/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

# Acessa a página dos campeões
driver.get('https://www.op.gg/champions')

# Scroll infinito até o fim da página
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Coleta os nomes e links dos campeões
champ_name = driver.find_elements(By.CSS_SELECTOR, 'a.flex.items-center.gap-2')


for champ in champ_name:
    try:
        name = champ.find_element(By.TAG_NAME, 'strong').text
        print(f"Nome: {name}")
    except Exception as e:
        print("Erro ao encontrar o nome ou o link do campeão.", e)
        continue

driver.quit()
