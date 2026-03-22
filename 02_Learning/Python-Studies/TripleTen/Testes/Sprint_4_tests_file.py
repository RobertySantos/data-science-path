import pandas as pd

data = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
mean_value = data.mean()
print(mean_value)
spacing_all = data - mean_value
print(spacing_all)
spacing_all_mean = spacing_all.mean()
print(spacing_all_mean)

contato = {
    'nome' : 'Tiago',
    'telefone' : '0000-0000',
    'contato_salve' : True
}

for chave, valor in contato.items():
    print('Chave: ', chave)
    print('Valor: ',valor)
    print('----------------')