<h1>Análise de Dados de Vendas</h1>
<h2>Objetivo</h2>
O objetivo deste projeto é analisar dados de vendas para identificar padrões, tendências e insights acionáveis. Usaremos um conjunto de dados para explorar a performance das vendas por região, produto e ao longo do tempo, além de criar visualizações para facilitar a interpretação dos dados.

<h2>Estrutura do Projeto</h2>
O projeto é estruturado da seguinte forma:

<h3>1.Obtenção de Dados:</h3> Utilizamos um arquivo CSV contendo os dados de vendas.
<h3>2.Análise Exploratória de Dados (EDA):</h3> Realizamos a análise exploratória dos dados para entender as principais métricas e variáveis.
<h3>3.Visualizações:</h3> Criamos gráficos para visualizar as tendências de vendas por região, produto e ao longo do tempo.

<h2>Instruções para Execução</h2>
<h3>1.Pré-requisitos:</h3>
Python 3.x
Bibliotecas Python: pandas, matplotlib, seaborn
Você pode instalar as bibliotecas necessárias usando o seguinte comando:
pip install pandas matplotlib seaborn

<h2>Obtenção dos Dados:</h2>

Os dados Csv estão contidos no repositorio do projeto

<h2>Execução:</h2>

Execute o script Python para realizar a análise e gerar as visualizações.

<h2>Código</h2>
O código para análise e visualização de dados é o seguinte:
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('vendas.csv')


print(df.head())


df['Data'] = pd.to_datetime(df['Data'])


df['Total_Vendas'] = df['Quantidade'] * df['Preço']


vendas_por_regiao = df.groupby('Região')['Total_Vendas'].sum().reset_index()
print(vendas_por_regiao)


vendas_por_produto = df.groupby('Produto')['Total_Vendas'].sum().reset_index()
print(vendas_por_produto)


vendas_por_data = df.groupby('Data')['Total_Vendas'].sum().reset_index()
print(vendas_por_data)


sns.set(style="whitegrid")


plt.figure(figsize=(10, 6))
sns.barplot(x='Região', y='Total_Vendas', data=vendas_por_regiao, palette='viridis')
plt.title('Total de Vendas por Região')
plt.xlabel('Região')
plt.ylabel('Total de Vendas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))
sns.barplot(x='Produto', y='Total_Vendas', data=vendas_por_produto, palette='viridis')
plt.title('Total de Vendas por Produto')
plt.xlabel('Produto')
plt.ylabel('Total de Vendas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 6))
sns.lineplot(x='Data', y='Total_Vendas', data=vendas_por_data, marker='o')
plt.title('Tendências de Vendas ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Total de Vendas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


<h2>Resultados</h2>
Os gráficos gerados pelo script proporcionam uma visão clara das vendas por região, produto e tendências ao longo do tempo. Essas visualizações ajudam a identificar quais regiões e produtos estão performando melhor e como as vendas estão evoluindo ao longo do tempo.



