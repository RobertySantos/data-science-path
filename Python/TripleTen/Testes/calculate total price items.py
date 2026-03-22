# escreva seu código aqui para definir uma função

def calculate_total_price(item_price,item_quantity):
    if item_quantity > 5:
        item_total_price = (item_price*item_quantity)*0.9
    else:
        item_total_price = item_price*item_quantity
    
    return item_total_price

# Defina os preços e as quantidades dos três itens
item_price_1 = 20.0
item_quantity_1 = 20

item_price_2 = 30.0
item_quantity_2 = 1

item_price_3 = 10.0
item_quantity_3 = 6


# Chame a função para cada item e armazene o resultado em uma variável
item_total_1 = calculate_total_price(item_price_1,item_quantity_1)# Escreva seu código aqui
item_total_2 = calculate_total_price(item_price_2,item_quantity_2)# Escreva seu código aqui
item_total_3 = calculate_total_price(item_price_3,item_quantity_3)# Escreva seu código aqui


# Imprima o preço total de cada item no carrinho
print(item_total_1)
print(item_total_2)
print(item_total_3)
