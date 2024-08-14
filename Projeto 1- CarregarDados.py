import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
'''1. Análise de Dados de Vendas
Objetivo: Analisar dados de vendas para identificar padrões, tendências e insights acionáveis.

O que fazer:

Obtenção de Dados: Utilize conjuntos de dados de vendas disponíveis online, como Kaggle ou UCI Machine Learning Repository.
Análise Exploratória: Use bibliotecas como pandas e matplotlib para realizar análise exploratória de dados (EDA). Examine as vendas por região, por produto, sazonalidade, etc.
Visualizações: Crie gráficos para visualizar as tendências de vendas ao longo do tempo e comparações entre diferentes categorias.
Previsão: Experimente modelos de previsão de vendas com scikit-learn ou statsmodels.'''

# Carregar dados do arquivo CSV para um DataFrame
df = pd.read_csv('vendas.csv')

# Exibir as primeiras linhas do DataFrame para verificar se os dados foram carregados corretamente
print(df.head())

# Convertendo a coluna 'Data' para o tipo datetime para facilitar operações de análise de data
df['Data'] = pd.to_datetime(df['Data'])

# Calculando o total de vendas como o produto da quantidade vendida pelo preço
df['Total_Vendas'] = df['Quantidade'] * df['Preço']

# Agrupar os dados por 'Região' e somar o total de vendas por região
vendas_por_regiao = df.groupby('Região')['Total_Vendas'].sum().reset_index()
# Exibir o total de vendas por região
print(vendas_por_regiao)

# Agrupar os dados por 'Produto' e somar o total de vendas por produto
vendas_por_produto = df.groupby('Produto')['Total_Vendas'].sum().reset_index()
# Exibir o total de vendas por produto
print(vendas_por_produto)

# Agrupar os dados por 'Data' e somar o total de vendas por data
vendas_por_data = df.groupby('Data')['Total_Vendas'].sum().reset_index()
# Exibir o total de vendas ao longo do tempo
print(vendas_por_data)

# Configurar o estilo dos gráficos usando seaborn para ter uma grade branca de fundo
sns.set(style="whitegrid")

# Criar um gráfico de barras para visualizar o total de vendas por região
plt.figure(figsize=(10, 6))  # Definir o tamanho da figura do gráfico
sns.barplot(x='Região', y='Total_Vendas', data=vendas_por_regiao, palette='viridis')  # Criar o gráfico de barras
plt.title('Total de Vendas por Região')  # Definir o título do gráfico
plt.xlabel('Região')  # Definir o rótulo do eixo x
plt.ylabel('Total de Vendas')  # Definir o rótulo do eixo y
plt.xticks(rotation=45)  # Rotacionar os rótulos do eixo x em 45 graus para melhor leitura
plt.tight_layout()  # Ajustar o layout para que todos os elementos se encaixem
plt.show()  # Exibir o gráfico

# Criar um gráfico de barras para visualizar o total de vendas por produto
plt.figure(figsize=(10, 6))  # Definir o tamanho da figura do gráfico
sns.barplot(x='Produto', y='Total_Vendas', data=vendas_por_produto, palette='viridis')  # Criar o gráfico de barras
plt.title('Total de Vendas por Produto')  # Definir o título do gráfico
plt.xlabel('Produto')  # Definir o rótulo do eixo x
plt.ylabel('Total de Vendas')  # Definir o rótulo do eixo y
plt.xticks(rotation=45)  # Rotacionar os rótulos do eixo x em 45 graus para melhor leitura
plt.tight_layout()  # Ajustar o layout para que todos os elementos se encaixem
plt.show()  # Exibir o gráfico

# Criar um gráfico de linha para visualizar as tendências de vendas ao longo do tempo
plt.figure(figsize=(12, 6))  # Definir o tamanho da figura do gráfico
sns.lineplot(x='Data', y='Total_Vendas', data=vendas_por_data, marker='o')  # Criar o gráfico de linha com marcadores
plt.title('Tendências de Vendas ao Longo do Tempo')  # Definir o título do gráfico
plt.xlabel('Data')  # Definir o rótulo do eixo x
plt.ylabel('Total de Vendas')  # Definir o rótulo do eixo y
plt.xticks(rotation=45)  # Rotacionar os rótulos do eixo x em 45 graus para melhor leitura
plt.tight_layout()  # Ajustar o layout para que todos os elementos se encaixem
plt.show()  # Exibir o gráfico
