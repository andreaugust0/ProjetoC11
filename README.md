# Projeto C11: Análise Exploratória da Ajuda Internacional à Ucrânia


Este projeto consiste em uma Análise Exploratória de Dados (EDA) sobre as alocações de ajuda internacional (financeira, militar e humanitária) destinadas à Ucrânia. Utilizando dados do arquivo `war.csv`, a análise é conduzida para identificar padrões, tendências e perfis de doadores.

## 📈 Análises Realizadas

O notebook investiga e responde a diversas perguntas-chave sobre o fluxo de ajuda:

1.  **Top Doadores:** Quais são os 5 países que mais alocaram fundos?
2.  **Menores Doadores:** Quais são os 5 países que menos alocaram fundos?
3.  **Promessas vs. Realidade (Commitments vs. Allocations):**
    * Quais países prometeram mais do que realmente alocaram?
    * Quais países alocaram mais do que prometeram?
4.  **Taxa de Cumprimento:** Identificação dos 10 países mais "controversos", ou seja, aqueles com a menor taxa de cumprimento de suas promessas.
5.  **Análise de Blocos (UE):** Comparação do volume total de ajuda (Financeira, Humanitária e Militar) entre países-membros da União Europeia e países não-membros.
6.  **Foco da Ajuda (Militar vs. Humanitário):**
    * Análise da prioridade de alocação (Militar vs. Humanitária) por blocos geopolíticos (UE, OTAN e Outros).
    * Visualização da distribuição de todos os países nesse espectro.
7.  **Correlação de Ajudas:** Análise da relação entre alocações financeiras e militares para os 10 maiores doadores financeiros.
8.  **Perfis de Doadores:** Classificação dos países em três perfis principais com base em sua maior contribuição:
    * **Armamentista:** Foco em ajuda militar.
    * **Financeiro:** Foco em ajuda financeira.
    * **Humanitário:** Foco em ajuda humanitária.
9.  **Top Doadores da UE:** Ranking dos 5 países da União Europeia que mais contribuíram.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Pandas:** Para limpeza, manipulação e análise dos dados.
* **NumPy:** Para operações numéricas e tratamento de dados.
* **Matplotlib:** Para a criação e personalização de todas as visualizações gráficas.

## 📊 Conjunto de Dados

O projeto utiliza o arquivo `war.csv`, que contém dados detalhados por país, incluindo:
* Status de membro da UE (`EU member_x`)
* PIB (`GDP in 2021($ billion)`)
* Valores prometidos (Commitments)
* Valores alocados (Allocations)
* Detalhamento por tipo de ajuda (Financeira, Militar, Humanitária)
