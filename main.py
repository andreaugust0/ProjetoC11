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

# Questão 6----------------------------------------------------------------------------------

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
# categories = ['Financeiro', 'Humanitário', 'Militar']
# x = range(len(categories))  # [0, 1, 2]
#
# bar_width = 0.35
#
# plt.figure(figsize=(10, 6))
# plt.bar([i - bar_width/2 for i in x], eu_values, width=bar_width, label='UE', color='royalblue')
# plt.bar([i + bar_width/2 for i in x], neu_values, width=bar_width, label='Não UE', color='orange')
#
# plt.xlabel('Tipo de Alocação')
# plt.ylabel('Total em $ bilhões')
# plt.title('Comparação de Alocações (UE vs Não UE)')
# plt.xticks(ticks=x, labels=categories)
# plt.legend()
#
# for i in range(len(x)):
#     plt.text(i - bar_width/2, eu_values[i] + 0.5, f'{eu_values[i]:.1f}', ha='center')
#     plt.text(i + bar_width/2, neu_values[i] + 0.5, f'{neu_values[i]:.1f}', ha='center')
#
# plt.tight_layout()
# plt.grid(axis='y', linestyle='--', alpha=0.6)
# plt.show()

# Questão 7----------------------------------------------------------------------------------

# Questão 8----------------------------------------------------------------------------------

# Questão 9----------------------------------------------------------------------------------



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