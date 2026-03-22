import requests

base_url = 'https://collectionapi.metmuseum.org/'
url = base_url + 'public/collection/v1/objects/437133'

response = requests.get(url)
print(response.json()['artistDisplayName'])

base_url = 'https://collectionapi.metmuseum.org/'
url = base_url + 'public/collection/v1/departments'# coloque seu código aqui

response = requests.get(url)

for dpt in response.json()['departments']:
    if 'Art' in dpt['displayName']:
        print(dpt['displayName'])

url = 'https://dummyjson.com/products'
params = {'limit': 3}
response = requests.get(url, params=params)
print(response.json())  