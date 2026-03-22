import json
import requests
from pathlib import Path

# 1. Pegamos o caminho da PASTA onde este arquivo .py está
BASE_DIR = Path(__file__).resolve().parent

# 2. Definimos o nome do arquivo que queremos criar
caminho_arquivo = BASE_DIR / "samsung_itens.json"
# busca dados na internet
response = requests.get('https://dummyjson.com/products/category/smartphones')

data = response.json() 
data_producst = data['products']
items = []
brand = 'Samsung'

for entry in data_producst:
    if entry['brand'] == brand:
        items.append(entry)
        
with open(caminho_arquivo, 'w') as file:
    json.dump(items, file)