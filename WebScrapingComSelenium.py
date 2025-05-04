from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.common.action_chains import ActionChains
import time

options = Options()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=options)


driver.get('https://www.op.gg/champions')

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        break

    last_height = new_height

champ_elements = driver.find_elements(By.CSS_SELECTOR, 'a.flex.items-center.gap-2')

for champ in champ_elements:
    try:
        name = champ.find_elements(By.Tag_NAME, 'strong').text
        href = champ.get_attribute('href')
        print(f"Nome: {name}")
        
    except:
        print("Erro ao encontrar o nome ou o link do campeão.")
        continue
driver.quit()
