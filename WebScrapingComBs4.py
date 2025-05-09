from bs4 import BeautifulSoup

url = 'https://www.op.gg/champions'  # Exemplo de URL estática, você pode ajustar para a que tem o HTML acessível
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Busca por todos os <a> com a classe específica que contém nome e link
champ_links = soup.find_all('a', class_='flex items-center gap-2')

for champ in champ_links:
    name_tag = champ.find('strong')
    if name_tag:
        name = name_tag.get_text(strip=True)
        print(f"Nome: {name}")
        link = champ['href']
