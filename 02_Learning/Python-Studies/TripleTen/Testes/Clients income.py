clients = [
    [32456, "Jack Wilson", 32, 150000, "Healthcare"],
    [34591, "Nina Brown", 45, 250000, "Telecom"],
    [37512, "Alex Smith", 39, 210000, "IT"],
    [39591, "Brian Perez", 29, 340000, "Transportation"],
    [45123, "Sarah Lee", 28, 120000, "Marketing"],
    [47635, "David Kim", 36, 180000, "Finance"],
    [49571, "Samantha Chen", 42, 220000, "Retail"],
    [50391, "Juan Rodriguez", 31, 160000, "Architecture"],
    [34556, "Lucas Hernandez", 37, 75000, "Education"],
    [64291, "Jessica Li", 25, 125000, "IT"],
    [74512, "Emma Davis", 47, 197000, "Finance"],
    [83191, "Sophia Perez", 34, 225000, "Transportation"],
    [91023, "Liam Kim", 29, 98000, "Retail"],
    [96435, "Ava Chen", 31, 175000, "Marketing"],
    [100571, "Noah Rodriguez", 28, 85000, "Architecture"],
    [101321, "Olivia Wilson", 44, 310000, "Telecom"],
    [104556, "William Brown", 38, 289000, "Finance"],
    [105491, "Emily Smith", 29, 193000, "Healthcare"],
    [107512, "Michael Perez", 53, 415000, "Transportation"]
]

incomes_per_field = {} # coloque aqui as rendas para cada área

for client in clients:
	field_name = client[-1]# primeiro, extraia o nome da área
	income = client[-2]# segundo, extraia a renda

	if field_name not in incomes_per_field:# verifique se o campo extraído NÃO está no dicionário incomes_per_field
		incomes_per_field[field_name] = [income]# adicione uma nova área como uma chave e defina uma lista como um valor
	else: # se o campo extraído está no dicionário incomes_per_field
		incomes_per_field[field_name].append(income)# adicione a nova renda à lista das rendas para uma determinada área
		

# não modifique o código abaixo. Ele imprime o resultado
print(incomes_per_field)