# Importe as bibliotecas necessárias
import pandas as pd
import openpyxl
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Carregue o conjunto de dados
data = pd.read_excel('arquivo_base_codigo.xlsx')

# Verifique as primeiras linhas do conjunto de dados
#print(data.head())

# Descreva estatísticas básicas dos dados
#print(data.describe())

# Verifique informações sobre os tipos de dados e valores ausentes
#print(data.info())

# Visualize a distribuição das categorias de qualidade ao longo dos anos
plt.figure(figsize=(12, 6))
sns.countplot(data=data.drop(["Localização", "Praia"], axis=1).melt(), x="variable", hue="value")
plt.title("Distribuição das Categorias de Qualidade ao Longo dos Anos")
plt.xlabel("Ano")
plt.ylabel("Contagem")
plt.xticks(rotation=45)
plt.legend(title="Qualidade")
plt.show()

# Calcule a correlação entre as variáveis
correlation_matrix = data.drop(["Localização", "Praia"], axis=1).corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=.5)
plt.title("Matriz de Correlação")
plt.show()

# Identifique valores ausentes
missing_data = data.isnull().sum()
print("Valores Ausentes por Coluna:")
print(missing_data)

# Realize outras análises conforme necessário

# Salve os resultados da análise exploratória
# Exemplo: data.to_excel("resultados_analise_exploratoria.xlsx", index=False)