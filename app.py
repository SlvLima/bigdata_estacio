import pandas as pd 

import numpy as np 

import matplotlib.pyplot as plt 

  

# Leitura do Excel 

df = pd.read_excel(r'/ClinicaMedica.xlsx') 

  

# Função para analisar uma coluna 

def analisar_coluna(df, coluna): 

    print(f"\nAnálise da coluna '{coluna}':") 

    print(f"Valores únicos: {df[coluna].unique()}") 

    print(f"Contagem de valores:\n{df[coluna].value_counts()}") 

    print(f"Número de valores ausentes: {df[coluna].isnull().sum()}") 

  

    # Plotar gráfico de barras para colunas categóricas 

    if df[coluna].dtype == 'object': 

        df[coluna].value_counts().plot(kind='bar') 

        plt.title(f'Distribuição de Valores na Coluna {coluna}') 

        plt.xlabel(coluna) 

        plt.ylabel('Contagem') 

        plt.show() 

     

    # Plotar histograma para colunas numéricas 

    elif df[coluna].dtype in ['int64', 'float64']: 

        plt.hist(df[coluna]) 

        plt.title(f'Distribuição de Valores na Coluna {coluna}') 

        plt.xlabel(coluna) 

        plt.ylabel('Frequência') 

        plt.show() 

  

# Analisar todas as colunas 

for coluna in df.columns: 

    analisar_coluna(df, coluna) 

  

# Informações gerais sobre o DataFrame 

print("\nInformações gerais sobre o DataFrame:") 

print(df.info()) 

  

# Estatísticas descritivas para colunas numéricas 

print("\nEstatísticas descritivas para colunas numéricas:") 

print(df.describe()) 

  

df.to_excel("Tabela limpa para bi.xlsx") 