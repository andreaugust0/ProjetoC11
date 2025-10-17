import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ds = pd.read_csv('war.csv', encoding='utf-8')
# Questão 1 -----------------------------------------------------------------------

# ds_filter = ds[['Country', 'Total bilateral allocations($ billion)']].copy()
#
# ds_filter['Total bilateral allocations($ billion)'] = ds_filter['Total bilateral allocations($ billion)'].replace('', 0)
# ds_filter['Total bilateral allocations($ billion)'] = pd.to_numeric(ds_filter['Total bilateral allocations($ billion)'], errors='coerce').fillna(0)
#
# top5 = ds_filter.sort_values(by='Total bilateral allocations($ billion)', ascending=False).head(5)
# print("Top 5 países que mais doaram:")
# print(top5)
#
# plt.figure(figsize=(10, 6))
# barras = plt.bar(top5['Country'], top5['Total bilateral allocations($ billion)'], color='green')
# plt.bar_label(barras, fmt='%.2f', padding=3, fontweight='bold')
# plt.xlabel('Países', fontweight='bold')
# plt.ylabel('Doações (em bilhões)', fontweight='bold')
# plt.title('Top 5 países que mais doaram para a Ucrânia (2024)', fontweight='bold')
# plt.grid(axis='y', linestyle='--', alpha=0.5)
# plt.tight_layout()
# plt.show()
#
# # Questão 2 –-------------------------------------------------------
# last5 = ds_filter.sort_values(by='Total bilateral allocations($ billion)', ascending=True).head(5)
# last5 = last5.iloc[::-1]
# print("\nTop 5 países que menos doaram:")
# print(last5)
#
# # Gráfico
# plt.figure(figsize=(10, 6))
# bars = plt.bar(last5['Country'], last5['Total bilateral allocations($ billion)'], color='red')
# plt.bar_label(bars, fmt='%.6f', padding=3, fontweight='bold')
# plt.xlabel('Países', fontweight='bold')
# plt.ylabel('Doações (em bilhões)', fontweight='bold')
# plt.title('Top 5 países que menos doaram para a Ucrânia', fontweight='bold')
# plt.grid(axis='y', linestyle='--', alpha=0.5)
# plt.tight_layout()
# plt.show()


# Questão 3----------------------------------------------------------------------------------

# Questão 4----------------------------------------------------------------------------------

# Questão 5----------------------------------------------------------------------------------

#Questão 6----------------------------------------------------------------------------------

# # Agrupar por status de membro da UE (1 = UE, 0 = Não UE)
# group_EU = ds.groupby('EU member_x')[[
#     'Financial allocations($ billion)',
#     'Humanitarian allocations($ billion)',
#     'Military allocations($ billion)'
# ]].sum()
#
# # Separar valores
# eu_values = group_EU.loc[1].values
# neu_values = group_EU.loc[0].values
#
# # Categorias
# categories = ['Financeiro', 'Humanitário', 'Militar']
# x = range(len(categories))
# bar_width = 0.35
#
# # Gráfico
# plt.figure(figsize=(10, 6))
# plt.bar([i - bar_width/2 for i in x], eu_values, width=bar_width, label='UE', color='blue')
# plt.bar([i + bar_width/2 for i in x], neu_values, width=bar_width, label='Não UE', color='gold')

# plt.xlabel('Tipo de Alocação')
# plt.ylabel('Total ($ bilhões)')
# plt.title('Comparação de Alocações (UE vs Não UE)')
# plt.xticks(x, categories)
# plt.legend()
#
# for i in range(len(x)):
#     plt.text(i - bar_width/2, eu_values[i] + 0.5, f'{eu_values[i]:.1f}', ha='center')
#     plt.text(i + bar_width/2, neu_values[i] + 0.5, f'{neu_values[i]:.1f}', ha='center')
#
# plt.tight_layout()
# plt.grid(axis='y', linestyle='--', alpha=0.6)
# plt.show()

#Questão 7----------------------------------------------------------------------------------

#Questão 8----------------------------------------------------------------------------------
# top_financial = ds.sort_values(by='Financial allocations($ billion)', ascending=False).head(10)
#
# x = top_financial['Country']
# financial = top_financial['Financial allocations($ billion)']
# military = top_financial['Military allocations($ billion)']
#
# # Definir a posição das barras
# x_indexes = np.arange(len(x))
# width = 0.35  # Largura das barras
#
# # Criar o gráfico
# plt.figure(figsize=(12, 6))
#
# bar_financial = plt.bar(x_indexes - width/2, financial, width=width, label='Financial', color='blue')
# bar_military = plt.bar(x_indexes + width/2, military, width=width, label='Military', color='gold')
#
# plt.bar_label(bar_financial, padding=3, fmt='%.1f')
# plt.bar_label(bar_military, padding=3, fmt='%.1f')
#
# # Ajustes visuais
# plt.xlabel('Country')
# plt.ylabel('Allocations ($ billion)')
# plt.title('Top 10 Countries: Financial vs Military Allocations')
# plt.xticks(ticks=x_indexes, labels=x, rotation=45, ha='right')
# plt.legend()
#
# # Mostrar o gráfico
# plt.tight_layout()
# plt.show()


#Questão 9----------------------------------------------------------------------------------
# Encontra o maior valor na linha, para as 3 colunas definidas, retorna o nome da coluna de maior valor
# allocation = ds[
#     ['Financial allocations($ billion)',
#      'Humanitarian allocations($ billion)',
#      'Military allocations($ billion)']
# ].idxmax(axis=1)
# 
# 
# def classificar(tipo):
#     if 'Military' in tipo:
#         return 'Armamentista'
#     elif 'Financial' in tipo:
#         return 'Financeiro'
#     elif 'Humanitarian' in tipo:
#         return 'Humanitário'
#     else:
#         return 'Indefinido'
# 
# 
# ds['Perfil'] = allocation.apply(classificar)
# 
# armamentista_df = ds[ds['Perfil'] == 'Armamentista']
# financeiro_df = ds[ds['Perfil'] == 'Financeiro']
# humanitario_df = ds[ds['Perfil'] == 'Humanitário']
# 
# def preparar_dados(df, coluna_valor):
#     # Substitui NaN por 0
#     df[coluna_valor] = df[coluna_valor].fillna(0)
# 
#     # Ordena e pega top 10
#     df_sorted = df.sort_values(by=coluna_valor, ascending=False)
#     top10 = df_sorted.head(10)
# 
#     # Soma total e soma top 10
#     total_geral = df[coluna_valor].sum()
#     total_top10 = top10[coluna_valor].sum()
# 
#     # Garante que "outros" nunca seja negativo
#     outros = max(total_geral - total_top10, 0)
# 
#     valores = list(top10[coluna_valor]) + [outros]
#     rotulos = list(top10['Country']) + ['Outros']
# 
#     return valores, rotulos
# 
# 
# fig, axes = plt.subplots(1, 3, figsize=(20, 7))
# 
# cores = {
#     'Armamentista': plt.cm.Reds,
#     'Financeiro': plt.cm.Blues,
#     'Humanitário': plt.cm.Greens
# }
# 
# 
# perfis = [
#     (armamentista_df, 'Military allocations($ billion)', 'Armamentista'),
#     (financeiro_df, 'Financial allocations($ billion)', 'Financeiro'),
#     (humanitario_df, 'Humanitarian allocations($ billion)', 'Humanitário')
# ]
# 
# for ax, (df, coluna, titulo) in zip(axes, perfis):
#     valores, rotulos = preparar_dados(df, coluna)
#     cmap = cores[titulo]
# 
#     cores_usadas = [cmap(1 - i/len(rotulos)) for i in range(len(rotulos))]
# 
#     wedges, texts, autotexts = ax.pie(
#         valores,
#         labels=None,
#         autopct='%1.1f%%',
#         startangle=90,
#         colors=cores_usadas,
#         textprops={'color': 'white', 'weight': 'bold'}
#     )
# 
#     ax.set_title(f'Perfil {titulo}', fontsize=14, fontweight='bold')
#     ax.axis('equal')
# 
#     ax.legend(
#         wedges,
#         rotulos,
#         title="Países",
#         loc="center left",
#         bbox_to_anchor=(1, 0.5),
#         fontsize=9
#     )
# 
# plt.suptitle('Distribuição dos Perfis de Doação — Top 10 por Categoria', fontsize=16, fontweight='bold')
# plt.tight_layout(rect=[0, 0, 1, 0.95])
# plt.show()

# Questão 10----------------------------------------------------------------------------------
# ds_UE = ds[ds['EU member_x'] == 1].copy()
# ds_country = ds_UE[['Country', 'Total bilateral allocations($ billion)']].copy()
#
# ds_country['Total bilateral allocations($ billion)'] = ds_country['Total bilateral allocations($ billion)'].replace('', 0)
# ds_country['Total bilateral allocations($ billion)'] = pd.to_numeric(ds_country['Total bilateral allocations($ billion)'], errors='coerce').fillna(0)
#
# top5 = ds_country.sort_values(by='Total bilateral allocations($ billion)', ascending=False).head(5)
#
# print("Top 5 países da União Europeia que mais doaram:")
# print(top5)
#
# plt.figure(figsize=(10, 6))
# barras = plt.bar(top5['Country'], top5['Total bilateral allocations($ billion)'], color='green')
# plt.bar_label(barras, fmt='%.2f', padding=3, fontweight='bold')
# plt.xlabel('Países', fontweight='bold')
# plt.ylabel('Doações (em bilhões)', fontweight='bold')
# plt.title('Top 5 países da União Europeia que mais doaram', fontweight='bold')
# plt.grid(axis='y', linestyle='--', alpha=0.5)
# plt.tight_layout()
# plt.show()