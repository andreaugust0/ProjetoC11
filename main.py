import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Questão 1 -----------------------------------------------------------------------
ds = np.loadtxt('war.csv',
                delimiter=',',
                dtype=str,
                encoding='utf-8')

np.set_printoptions(precision=9, suppress=True) #evita que os numero sejam mostrados em forma de notação cientifica e limita 4 casas decimais
newDs = ds[1:, [0,11]] #filtrando as duas colunas
newDs[:, 1] = np.where(newDs[:, 1] == '', '0', newDs[:, 1]) #trocando vazio por zero
values = newDs[:,1].astype(float) #de string pra float

indices = values.argsort()[::-1] #pegando os indices ordenados de forma decrescente
top5_indices = indices[:5] #pega os 5 maiores índices
top5 = newDs[top5_indices] #top 5 maiores países e seus valores

print("Top 5 países que mais doaram: ")
print(top5)

# Separando nomes e valores
countries = top5[:, 0]
donations = top5[:, 1].astype(float)

# Criando o gráfico de barras
# plt.figure(figsize=(10, 6))
# plt.bar(countries, donations, color='skyblue')
# plt.xlabel('Países')
# plt.ylabel('Doações (em bilhões)')
# plt.title('Top 5 países que mais doaram para a Ucrânia (2024)')
# plt.grid(axis='y', linestyle='--', alpha=0.5)
# plt.tight_layout()
#
# # Exibindo o gráfico
# plt.show()

#Questão 2 -----------------------------------------------------------

last5_indices = indices[-5:][::-1] #5 ultimos de forma crescente
last5 = newDs[last5_indices] #Top 5 menores países e seus valores

print('')
print("Top 5 países que menos doaram: ")
print(last5)

#Questão 3----------------------------------------------------------------------------------

#Questão 4----------------------------------------------------------------------------------

#Questão 5----------------------------------------------------------------------------------

#Questão 6----------------------------------------------------------------------------------

#Questão 7----------------------------------------------------------------------------------

#Questão 8----------------------------------------------------------------------------------

#Questão 9----------------------------------------------------------------------------------

#Questão 10----------------------------------------------------------------------------------



