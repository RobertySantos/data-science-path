import pandas as pd
import scipy.stats
import streamlit as st
import time
import plotly.express as px
from pathlib import Path

path = Path(__file__).parent / 'data' / 'vehicles.csv' # caminho para o arquivo de dados    
vehicles_data = pd.read_csv(path)#lendos os dados de veículos
st.title('Análise de Veículos Usados') # título do app
st.write('Este aplicativo analisa dados de veículos usados para ajudar os compradores a tomar decisões informadas.') # descrição do app
st.header('Visão Geral dos Dados') # seção de visão geral dos dados

build_histogram = st.checkbox('Exibir Histograma de Quilometragem') # checkbox para exibir o histograma
if build_histogram: #se a caixa de seleção for marcada
    fig = px.histogram(vehicles_data, x="odometer", nbins=50, title='Histograma de Quilometragem') # criar um histograma
    st.plotly_chart(fig) # exibindo o histograma

build_scatter = st.checkbox('Exibir Gráfico de Dispersão de Preço vs Quilometragem') # checkbox para exibir o gráfico de dispersão
if build_scatter: # se a caixa de seleção for marcada
    fig = px.scatter(vehicles_data, x="odometer", y="price", title='Preço vs Quilometragem') # criar um gráfico de dispersão
    st.plotly_chart(fig) # exibindo o gráfico de dispersão
