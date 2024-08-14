<h1>Análise de Dados de Vendas</h1>
Objetivo
O objetivo deste projeto é analisar dados de vendas para identificar padrões, tendências e insights acionáveis. Usaremos um conjunto de dados para explorar a performance das vendas por região, produto e ao longo do tempo, além de criar visualizações para facilitar a interpretação dos dados.

#Estrutura do Projeto
O projeto é estruturado da seguinte forma:

1.Obtenção de Dados: Utilizamos um arquivo CSV contendo os dados de vendas.
2.Análise Exploratória de Dados (EDA): Realizamos a análise exploratória dos dados para entender as principais métricas e variáveis.
3.Visualizações: Criamos gráficos para visualizar as tendências de vendas por região, produto e ao longo do tempo.

#Instruções para Execução
1.Pré-requisitos:
.Python 3.x
.Bibliotecas Python: pandas, matplotlib, seaborn
Você pode instalar as bibliotecas necessárias usando o seguinte comando:
pip install pandas matplotlib seaborn

#Obtenção dos Dados:

Certifique-se de ter o arquivo vendas.csv no mesmo diretório do script Python. Este arquivo deve conter as colunas Data, Região, Produto, Quantidade e Preço.

#Execução:

Execute o script Python para realizar a análise e gerar as visualizações.

#Código
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


#Resultados
Os gráficos gerados pelo script proporcionam uma visão clara das vendas por região, produto e tendências ao longo do tempo. Essas visualizações ajudam a identificar quais regiões e produtos estão performando melhor e como as vendas estão evoluindo ao longo do tempo.



