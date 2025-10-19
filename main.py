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


# Questão 3 e 4 ----------------------------------------------------------------------------------
# # converter colunas numéricas
# df['GDP in 2021($ billion)'] = df['GDP in 2021($ billion)'].astype(str).str.replace(',', '').astype(float)
# df['Total bilateral commitments($ billion)'] = pd.to_numeric(df['Total bilateral commitments($ billion)'], errors='coerce').fillna(0)
# df['Total bilateral allocations($ billion)'] = pd.to_numeric(df['Total bilateral allocations($ billion)'], errors='coerce').fillna(0)

# # separar países por condição
# paises_commitments_maior = df[df['Total bilateral commitments($ billion)'] > df['Total bilateral allocations($ billion)']]
# paises_allocations_maior = df[df['Total bilateral allocations($ billion)'] > df['Total bilateral commitments($ billion)']]

# # selecionar top 5 de cada
# top5_commitments_maior = paises_commitments_maior.nlargest(5, 'Total bilateral commitments($ billion)')
# top5_allocations_maior = paises_allocations_maior.nlargest(5, 'Total bilateral allocations($ billion)')

# print("=" * 80)
# print("PAÍSES COM COMMITMENTS > ALLOCATIONS")
# print("=" * 80)
# print(f"{'País':<20} {'Commitments ($B)':<18} {'Allocations ($B)':<18} {'Diferença ($B)':<15}")
# print("-" * 80)
# for _, row in top5_commitments_maior.iterrows():
#     diff = row['Total bilateral commitments($ billion)'] - row['Total bilateral allocations($ billion)']
#     print(f"{row['Country']:<20} ${row['Total bilateral commitments($ billion)']:<16.2f} ${row['Total bilateral allocations($ billion)']:<16.2f} +${diff:<13.2f}")

# print("\n" + "=" * 80)
# print("PAÍSES COM ALLOCATIONS > COMMITMENTS")
# print("=" * 80)
# print(f"{'País':<20} {'Allocations ($B)':<18} {'Commitments ($B)':<18} {'Diferença ($B)':<15}")
# print("-" * 80)
# for _, row in top5_allocations_maior.iterrows():
#     diff = row['Total bilateral allocations($ billion)'] - row['Total bilateral commitments($ billion)']
#     print(f"{row['Country']:<20} ${row['Total bilateral allocations($ billion)']:<16.2f} ${row['Total bilateral commitments($ billion)']:<16.2f} +${diff:<13.2f}")

# # gráfico
# plt.figure(figsize=(14, 8))

# # combinar os top 5 de cada categoria
# top_paises = pd.concat([top5_commitments_maior, top5_allocations_maior])
# top_paises = top_paises.sort_values('Total bilateral commitments($ billion)', ascending=False)

# x = np.arange(len(top_paises))
# width = 0.35

# bars1 = plt.bar(x - width/2, top_paises['Total bilateral commitments($ billion)'],
#                width, label='Commitments', color='#2E86AB', alpha=0.8, edgecolor='black')
# bars2 = plt.bar(x + width/2, top_paises['Total bilateral allocations($ billion)'],
#                width, label='Allocations', color='#FFD700', alpha=0.8, edgecolor='black')  # Amarelo no lugar do rosa

# plt.xlabel('Países', fontsize=12, fontweight='bold')
# plt.ylabel('Valor ($ Bilhões)', fontsize=12, fontweight='bold')
# plt.title('Comparação: Commitments vs Allocations - Países com Maiores Diferenças', fontsize=14, fontweight='bold')
# plt.xticks(x, top_paises['Country'], rotation=45, ha='right')
# plt.legend(fontsize=11)
# plt.grid(axis='y', alpha=0.3)

# for bars in [bars1, bars2]:
#     for bar in bars:
#         height = bar.get_height()
#         if height > 0.1:  # Só mostrar valores acima de 0.1 bilhão
#             plt.text(bar.get_x() + bar.get_width()/2., height + 1,
#                    f'${height:.1f}B', ha='center', va='bottom', fontsize=9, fontweight='bold')

# plt.tight_layout()
# plt.show()

# # estatísticas
# print("\n" + "=" * 80)
# print("ESTATÍSTICAS GERAIS")
# print("=" * 80)
# print(f"Total de países analisados: {len(df)}")
# print(f"Países com Commitments > Allocations: {len(paises_commitments_maior)}")
# print(f"Países com Allocations > Commitments: {len(paises_allocations_maior)}")
# print(f"Países com valores iguais: {len(df[df['Total bilateral commitments($ billion)'] == df['Total bilateral allocations($ billion)']])}")

# #mostrar país com a maior diferença
# if len(paises_commitments_maior) > 0:
#     maior_diff_commitments = paises_commitments_maior.loc[
#         (paises_commitments_maior['Total bilateral commitments($ billion)'] -
#          paises_commitments_maior['Total bilateral allocations($ billion)']).idxmax()
#     ]
#     diff = maior_diff_commitments['Total bilateral commitments($ billion)'] - maior_diff_commitments['Total bilateral allocations($ billion)']
#     print(f"\nMaior diferença (C > A): {maior_diff_commitments['Country']} - +${diff:.2f}B")

# if len(paises_allocations_maior) > 0:
#     maior_diff_allocations = paises_allocations_maior.loc[
#         (paises_allocations_maior['Total bilateral allocations($ billion)'] -
#          paises_allocations_maior['Total bilateral commitments($ billion)']).idxmax()
#     ]
#     diff = maior_diff_allocations['Total bilateral allocations($ billion)'] - maior_diff_allocations['Total bilateral commitments($ billion)']
#     print(f"Maior diferença (A > C): {maior_diff_allocations['Country']} - +${diff:.2f}B")

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

# df['GDP in 2021($ billion)'] = df['GDP in 2021($ billion)'].astype(str).str.replace(',', '').astype(float)
# df['Humanitarian allocations($ billion)'] = pd.to_numeric(df['Humanitarian allocations($ billion)'],
#                                                           errors='coerce').fillna(0)
# df['Military allocations($ billion)'] = pd.to_numeric(df['Military allocations($ billion)'], errors='coerce').fillna(0)
#
# # lista de países da OTAN (baseado no dataset)
# paises_otan = [
#     'United States', 'Canada', 'United Kingdom', 'Germany', 'France', 'Italy',
#     'Spain', 'Netherlands', 'Belgium', 'Portugal', 'Greece', 'Turkey',
#     'Poland', 'Czech Republic', 'Hungary', 'Bulgaria', 'Romania', 'Slovakia',
#     'Slovenia', 'Croatia', 'Lithuania', 'Latvia', 'Estonia', 'Norway',
#     'Denmark', 'Iceland'
# ]
#
# # adicionar colunas de classificação
# df['UE'] = df['EU member_x'] == 1
# df['OTAN'] = df['Country'].isin(paises_otan)
# df['Razao_Militar_Humanitario'] = np.where(
#     df['Humanitarian allocations($ billion)'] > 0,
#     df['Military allocations($ billion)'] / df['Humanitarian allocations($ billion)'],
#     float('inf')  # Se ajuda humanitária = 0, razão é infinita
# )
#
# # classificar países por foco
# df['Foco'] = np.where(
#     df['Razao_Militar_Humanitario'] > 1, 'Militar',
#     np.where(df['Razao_Militar_Humanitario'] == 1, 'Equilibrado', 'Humanitário')
# )
#
# # filtrar países com dados significativos (pelo menos 0.1B em uma das categorias)
# df_significativo = df[
#     (df['Military allocations($ billion)'] > 0.1) |
#     (df['Humanitarian allocations($ billion)'] > 0.1)
#     ]
#
# print("=" * 80)
# print("ANÁLISE: FOCO MILITAR vs HUMANITÁRIO")
# print("=" * 80)
#
# print("\n1. DISTRIBUIÇÃO POR GRUPOS GEOPOLÍTICOS:")
# print("-" * 50)
#
# grupos = {
#     'UE': df_significativo['UE'] == True,
#     'OTAN': df_significativo['OTAN'] == True,
#     'Fora UE e OTAN': (df_significativo['UE'] == False) & (df_significativo['OTAN'] == False)
# }
#
# # contar número de países por grupo
# num_paises_por_grupo = {}
# for nome_grupo, condicao in grupos.items():
#     grupo = df_significativo[condicao]
#     num_paises_por_grupo[nome_grupo] = len(grupo)
#
# for nome_grupo, condicao in grupos.items():
#     grupo = df_significativo[condicao]
#     if len(grupo) > 0:
#         total_militar = grupo['Military allocations($ billion)'].sum()
#         total_humanitario = grupo['Humanitarian allocations($ billion)'].sum()
#         total_geral = total_militar + total_humanitario
#
#         print(f"\n{nome_grupo} ({len(grupo)} países):")
#         print(f"  Militar: ${total_militar:.2f}B ({total_militar / total_geral * 100:.1f}%)")
#         print(f"  Humanitário: ${total_humanitario:.2f}B ({total_humanitario / total_geral * 100:.1f}%)")
#         if total_humanitario > 0:
#             print(f"  Razão M/H: {total_militar / total_humanitario:.2f}")
#         else:
#             print(f"  Razão M/H: Infinita (sem ajuda humanitária)")
#
# #gráfico 1
# plt.figure(figsize=(14, 10))
#
# grupos_grafico = ['UE', 'OTAN', 'Fora UE e OTAN']
# valores_militar = []
# valores_humanitario = []
# num_paises = []
#
# for nome_grupo in grupos_grafico:
#     condicao = grupos[nome_grupo]
#     grupo = df_significativo[condicao]
#     if len(grupo) > 0:
#         valores_militar.append(grupo['Military allocations($ billion)'].sum())
#         valores_humanitario.append(grupo['Humanitarian allocations($ billion)'].sum())
#         num_paises.append(len(grupo))
#
# x = np.arange(len(grupos_grafico))
# width = 0.35
#
# # CORES DA BANDEIRA DA UCRÂNIA: Azul (#0057B7) e Amarelo (#FFD700)
# bars1 = plt.bar(x - width / 2, valores_militar, width, label='Alocações Militares',
#                 color='#0057B7', alpha=0.9, edgecolor='#003D82', linewidth=1.5)
# bars2 = plt.bar(x + width / 2, valores_humanitario, width, label='Alocações Humanitárias',
#                 color='#FFD700', alpha=0.9, edgecolor='#CCAC00', linewidth=1.5)
#
# plt.xlabel('Grupo Geopolítico', fontsize=12, fontweight='bold')
# plt.ylabel('Valor Total ($ Bilhões)', fontsize=12, fontweight='bold')
#
# titulo = 'Comparação: Alocações Militares vs Humanitárias por Grupo Geopolítico\n'
# titulo += f'🇺🇦 UE: {num_paises[0]} países | OTAN: {num_paises[1]} países | Outros: {num_paises[2]} países'
# plt.title(titulo, fontsize=14, fontweight='bold', pad=20)
#
# labels_eixo_x = [f'UE\n{num_paises[0]} países',
#                  f'OTAN\n{num_paises[1]} países',
#                  f'Outros\n{num_paises[2]} países']
# plt.xticks(x, labels_eixo_x)
# plt.legend(fontsize=11)
# plt.grid(axis='y', alpha=0.3)
#
# for bars in [bars1, bars2]:
#     for bar in bars:
#         height = bar.get_height()
#         if height > 1:
#             plt.text(bar.get_x() + bar.get_width() / 2., height + 2,
#                      f'${height:.1f}B', ha='center', va='bottom', fontsize=10, fontweight='bold')
#
# plt.tight_layout()
# plt.show()
#
# #gráfico 2
# plt.figure(figsize=(12, 10))
#
# try:
#     max_val_militar = df_significativo['Military allocations($ billion)'].max()
#     max_val_humanitario = df_significativo['Humanitarian allocations($ billion)'].max()
#     max_val = max(max_val_militar, max_val_humanitario)
#
#     max_val = max_val * 1.1
# except:
#     max_val = 100
#
# cores = []
# for _, row in df_significativo.iterrows():
#     if row['UE'] and row['OTAN']:
#         cores.append('#0057B7')
#     elif row['UE']:
#         cores.append('#4A8BDB')
#     elif row['OTAN']:
#         cores.append('#003D82')
#     else:
#         cores.append('#FFD700')
#
# plt.scatter(df_significativo['Humanitarian allocations($ billion)'],
#             df_significativo['Military allocations($ billion)'],
#             c=cores, s=100, alpha=0.8, edgecolors='black', linewidth=0.8)
#
# plt.plot([0, max_val], [0, max_val], 'k--', alpha=0.5, label='Linha de Igualdade')
#
# plt.xlabel('Alocações Humanitárias ($ Bilhões)', fontsize=12, fontweight='bold')
# plt.ylabel('Alocações Militares ($ Bilhões)', fontsize=12, fontweight='bold')
# plt.title('Relação entre Alocações Militares e Humanitárias\n' +
#           '🇺🇦 Países Mais Impactantes por Grupo',
#           fontsize=14, fontweight='bold', pad=20)
# plt.grid(alpha=0.3)
#
# from matplotlib.patches import Patch
#
# legend_elements = [
#     Patch(facecolor='#0057B7',
#           label=f'UE + OTAN ({num_paises_por_grupo["UE"] + num_paises_por_grupo["OTAN"] - len(df_significativo[(df_significativo["UE"] == True) & (df_significativo["OTAN"] == True)])} países)'),
#     Patch(facecolor='#4A8BDB',
#           label=f'UE apenas ({len(df_significativo[(df_significativo["UE"] == True) & (df_significativo["OTAN"] == False)])} países)'),
#     Patch(facecolor='#003D82',
#           label=f'OTAN apenas ({len(df_significativo[(df_significativo["UE"] == False) & (df_significativo["OTAN"] == True)])} países)'),
#     Patch(facecolor='#FFD700', label=f'Fora UE/OTAN ({num_paises_por_grupo["Fora UE e OTAN"]} países)')
# ]
#
# plt.legend(handles=legend_elements, loc='upper left')
#
# paises_impactantes = {}
#
# ue_otan = df_significativo[(df_significativo['UE'] == True) & (df_significativo['OTAN'] == True)]
# if len(ue_otan) > 0:
#     ue_otan['Soma_Total'] = ue_otan['Military allocations($ billion)'] + ue_otan['Humanitarian allocations($ billion)']
#     pais_ue_otan = ue_otan.loc[ue_otan['Soma_Total'].idxmax()]
#     paises_impactantes['UE+OTAN'] = pais_ue_otan
#
# ue_apenas = df_significativo[(df_significativo['UE'] == True) & (df_significativo['OTAN'] == False)]
# if len(ue_apenas) > 0:
#     ue_apenas['Soma_Total'] = ue_apenas['Military allocations($ billion)'] + ue_apenas['Humanitarian allocations($ billion)']
#     pais_ue_apenas = ue_apenas.loc[ue_apenas['Soma_Total'].idxmax()]
#     paises_impactantes['UE'] = pais_ue_apenas
#
# otan_apenas = df_significativo[(df_significativo['UE'] == False) & (df_significativo['OTAN'] == True)]
# if len(otan_apenas) > 0:
#     otan_apenas['Soma_Total'] = otan_apenas['Military allocations($ billion)'] + otan_apenas['Humanitarian allocations($ billion)']
#     pais_otan_apenas = otan_apenas.loc[otan_apenas['Soma_Total'].idxmax()]
#     paises_impactantes['OTAN'] = pais_otan_apenas
#
# fora_ue_otan = df_significativo[(df_significativo['UE'] == False) & (df_significativo['OTAN'] == False)]
# if len(fora_ue_otan) > 0:
#     fora_ue_otan['Soma_Total'] = fora_ue_otan['Military allocations($ billion)'] + fora_ue_otan['Humanitarian allocations($ billion)']
#     pais_fora_ue_otan = fora_ue_otan.loc[fora_ue_otan['Soma_Total'].idxmax()]
#     paises_impactantes['Fora'] = pais_fora_ue_otan
#
# cores_organizacao = {
#     'UE+OTAN': '#0057B7',
#     'UE': '#4A8BDB',
#     'OTAN': '#003D82',
#     'Fora': '#FFD700'
# }
#
# posicoes_annotate = {
#     'UE+OTAN': (15, 10),
#     'UE': (-25, 10),
#     'OTAN': (15, -15),
#     'Fora': (-25, -15)
# }
#
# for grupo, pais_data in paises_impactantes.items():
#     cor_fundo = cores_organizacao[grupo]
#
#     plt.annotate(pais_data['Country'],
#                  (pais_data['Humanitarian allocations($ billion)'], pais_data['Military allocations($ billion)']),
#                  xytext=posicoes_annotate[grupo], textcoords='offset points', fontsize=11, fontweight='bold',
#                  bbox=dict(boxstyle='round,pad=0.4', facecolor=cor_fundo, alpha=0.9, edgecolor='black'),
#                  arrowprops=dict(arrowstyle='->', color='black', alpha=0.7, linewidth=1.5))
#
# plt.tight_layout()
# plt.show()
#
# print("\n" + "=" * 80)
# print("CONCLUSÕES E TENDÊNCIAS OBSERVADAS")
# print("=" * 80)
#
# print("\nPAÍSES MAIS IMPACTANTES POR GRUPO:")
# for grupo, pais_data in paises_impactantes.items():
#     soma_total = pais_data['Military allocations($ billion)'] + pais_data['Humanitarian allocations($ billion)']
#     print(f"- {grupo}: {pais_data['Country']} (${soma_total:.1f}B total)")
#
# for nome_grupo, condicao in grupos.items():
#     grupo = df_significativo[condicao]
#     if len(grupo) > 0:
#         razoes_finitas = grupo[grupo['Razao_Militar_Humanitario'] != float('inf')]['Razao_Militar_Humanitario']
#         if len(razoes_finitas) > 0:
#             media_razao = razoes_finitas.mean()
#         else:
#             media_razao = float('inf')
#
#         percentual_militar = (grupo['Foco'] == 'Militar').mean() * 100
#
#         print(f"\n{nome_grupo} ({len(grupo)} países):")
#         if media_razao != float('inf'):
#             print(f"  - Razão Média Militar/Humanitário: {media_razao:.2f}")
#         else:
#             print(f"  - Razão Média Militar/Humanitário: Infinita")
#         print(f"  - % de países com foco militar: {percentual_militar:.1f}%")
#
#         if media_razao > 1:
#             print(f"  → TENDÊNCIA: Foco em ajuda MILITAR")
#         else:
#             print(f"  → TENDÊNCIA: Foco em ajuda HUMANITÁRIA")
#
# print(f"\nRESUMO GEOESTRATÉGICO:")
# print(f"- UE: {num_paises_por_grupo['UE']} países analisados")
# print(f"- OTAN: {num_paises_por_grupo['OTAN']} países analisados")
# print(f"- Fora UE/OTAN: {num_paises_por_grupo['Fora UE e OTAN']} países analisados")
# print("- Países da OTAN tendem a ter maior foco militar devido à natureza da aliança")
# print("- Países da UE mostram padrão misto, com alguns focando mais em ajuda humanitária")
# print("- Países fora dessas alianças variam amplamente, dependendo de interesses nacionais")


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