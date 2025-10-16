import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Questão 1 -----------------------------------------------------------------------
# ds = np.loadtxt('war.csv',
#                 delimiter=',',
#                 dtype=str,
#                 encoding='utf-8')
#
# np.set_printoptions(precision=9, suppress=True) #evita que os numero sejam mostrados em forma de notação cientifica e limita 4 casas decimais
# newDs = ds[1:, [0,11]] #filtrando as duas colunas
# newDs[:, 1] = np.where(newDs[:, 1] == '', '0', newDs[:, 1]) #trocando vazio por zero
# values = newDs[:,1].astype(float) #de string pra float
#
# indices = values.argsort()[::-1] #pegando os indices ordenados de forma decrescente
# top5_indices = indices[:5] #pega os 5 maiores índices
# top5 = newDs[top5_indices] #top 5 maiores países e seus valores
#
# print("Top 5 países que mais doaram: ")
# print(top5)
#
# # Separando nomes e valores
# countries = top5[:, 0]
# donations = top5[:, 1].astype(float)
#
# #Criando o gráfico de barras
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

# last5_indices = indices[-5:][::-1] #5 ultimos de forma crescente
# last5 = newDs[last5_indices] #Top 5 menores países e seus valores
#
# print('')
# print("Top 5 países que menos doaram: ")
# print(last5)

#Questão 3----------------------------------------------------------------------------------

#Questão 4----------------------------------------------------------------------------------

#Questão 5----------------------------------------------------------------------------------

#Questão 6----------------------------------------------------------------------------------
# ds = pd.read_csv('war.csv', delimiter=',')
#
# ds_euMember = ds['EU member_x'] == 1
#
# contry_EU = ds[ds_euMember]['Country']
#
# ds_NeuMember = ds['EU member_x'] == 0
#
# contry_NEU = ds[ds_NeuMember]['Country']
#
# financial_EU = ds[ds_euMember]['Financial allocations($ billion)']
#
# humanitarian_EU = ds[ds_euMember]['Humanitarian allocations($ billion)']
#
# military_EU = ds[ds_euMember]['Military allocations($ billion)']
#
# financial_NEU = ds[ds_NeuMember]['Financial allocations($ billion)']
#
# humanitarian_NEU = ds[ds_NeuMember]['Humanitarian allocations($ billion)']
#
# military_NEU = ds[ds_NeuMember]['Military allocations($ billion)']
#
# print("Soma total (UE):")
# print("Financeiro:", financial_EU.sum())
# print("Humanitário:", humanitarian_EU.sum())
# print("Militar:", military_EU.sum())
#
# print("Soma total (Não UE):")
# print("Financeiro:", financial_NEU.sum())
# print("Humanitário:", humanitarian_NEU.sum())
# print("Militar:", military_NEU.sum())
#
# eu_values = [
#     financial_EU.sum(),
#     humanitarian_EU.sum(),
#     military_EU.sum()
# ]
#
# neu_values = [
#     financial_NEU.sum(),
#     humanitarian_NEU.sum(),
#     military_NEU.sum()
# ]
#
# # Rótulos para os tipos de alocação
# categories = ['Financeiro', 'Humanitário', 'Militar']
# x = range(len(categories))  # [0, 1, 2]
#
# # Criar o gráfico
# bar_width = 0.35
#
# plt.figure(figsize=(10, 6))
# plt.bar([i - bar_width/2 for i in x], eu_values, width=bar_width, label='UE', color='royalblue')
# plt.bar([i + bar_width/2 for i in x], neu_values, width=bar_width, label='Não UE', color='orange')
#
# # Adicionando rótulos
# plt.xlabel('Tipo de Alocação')
# plt.ylabel('Total em $ bilhões')
# plt.title('Comparação de Alocações (UE vs Não UE)')
# plt.xticks(ticks=x, labels=categories)
# plt.legend()
#
# # Adicionar valores nas barras
# for i in range(len(x)):
#     plt.text(i - bar_width/2, eu_values[i] + 0.5, f'{eu_values[i]:.1f}', ha='center')
#     plt.text(i + bar_width/2, neu_values[i] + 0.5, f'{neu_values[i]:.1f}', ha='center')
#
# plt.tight_layout()
# plt.grid(axis='y', linestyle='--', alpha=0.6)
# plt.show()




#Questão 7----------------------------------------------------------------------------------

#Questão 8----------------------------------------------------------------------------------

#Questão 9----------------------------------------------------------------------------------

#Questão 10----------------------------------------------------------------------------------
# 1) Top 5 países que mais doaram - feito
#
# 2) Top 5 países que menos doaram - feito
#
# 3) Países que prometeram mais do que realmente doaram
#
# 4) Países que prometeram menos do que realmente doaram
#
# 5) Qual a relação do PIB do país com suas doações(porcentagem do PIB)
#
# 6) Padrões de Ajuda na União Europeia: Como os membros da União Europeia se comparam aos países não
# membros em termos de alocações financeiras, humanitárias e militares como proporção do total de suas ajudas
#
# 7) Foco da Ajuda: Militar vs. Humanitária: Que países priorizam as alocações militares em
# detrimento das humanitárias, e vice-versa? Existe alguma tendência regional ou geopolítica observável?
#
# 8) países que dão mais ajuda financeira também tendem a dar mais ajuda militar
#
# 9) Análise Comparativa de Perfis de Ajuda: É possível agrupar os países em diferentes "perfis de doadores"
# com base na composição de sua ajuda (por exemplo, "humanitários", "desenvolvimentistas", "estrategistas militares")?
#
# 10) 5 países da uniao europeia que mais contribuem


