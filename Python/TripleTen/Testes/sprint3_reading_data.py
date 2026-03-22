import seaborn as sns
import pandas as pd
import matplotlib as plt

# 1. Criando um DataFrame do Pandas do zero
dados_vendas = {
    'Mes': ['Jan', 'Fev', 'Mar', 'Abr', 'Jan', 'Fev', 'Mar', 'Abr'],
    'Vendas': [1500, 1800, 1200, 2100, 1700, 1600, 1400, 2500],
    'Filial': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B']
}

df = pd.DataFrame(dados_vendas)

# 2. Usando o Seaborn para plotar
# O parâmetro 'hue' separa os dados por cores baseadas em uma coluna
sns.lineplot(data=df, x="Mes", y="Vendas", hue="Filial", marker="o")

# 3. Personalizando com Matplotlib
plt.pyplot.title("Evolução de Vendas por Filial")
plt.pyplot.grid(True)
plt.pyplot.show()


