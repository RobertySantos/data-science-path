# Análise de Veículos Usados 🚗

Este projeto é uma aplicação web interativa desenvolvida como parte da **Sprint 5 do programa TripleTen**. O objetivo é explorar e visualizar dados de um conjunto de anúncios de venda de veículos, permitindo que o usuário identifique padrões de quilometragem e preço através de ferramentas visuais.

## 🚀 Funcionalidades
- **Histograma de Quilometragem:** Visualização da distribuição do odômetro dos veículos.
- **Gráfico de Dispersão:** Análise da correlação entre o preço de venda e a quilometragem rodada.
- **Interatividade:** Filtros controlados por caixas de seleção (checkboxes) para alternar visualizações.

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**
- **Streamlit:** Framework para criação da interface web.
- **Pandas:** Manipulação e limpeza de dados.
- **Plotly Express:** Criação de gráficos interativos.
- **Pathlib:** Gerenciamento inteligente de caminhos de arquivos.

## 📂 Estrutura do Projeto
```text
Render/
├── app.py           # Código principal do Streamlit
├── data/            # Conjunto de dados (vehicles.csv)
├── notebooks/       # Jupyter Notebooks de análise exploratória
├── requirements.txt # Dependências do projeto
└── venv/            # Ambiente virtual (não versionado)
