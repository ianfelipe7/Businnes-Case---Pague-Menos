'''
Case 2 - Elasticidade-Preço da Demanda
Este script tenm por objetivo identificar produtos sensíveis ao preço e sugere ajustes de precificação baseados em sua elasticidade, com o objetivo de aumentar a receita do varejo farmacêutico.

Desenvolvido por: Ian Felipe - Analista de Dados  |  Versão: 1.0 em 29/07/2025 
'''

import pandas as pd
import numpy as np

# Carregar a base de dados

input = r'C:\Users\ian.teteo\Desktop\Ian Felipe - Pole\Dev BI\Python\Case - Pague Menos\Base de Dados_Case 2.csv'
output = r'C:\Users\ian.teteo\Desktop\Ian Felipe - Pole\Dev BI\Python\Case - Pague Menos\Output_Case2_Precificacao.xlsx'
df = pd.read_csv(input)

# --------------------------------------------------------------------------------------- Fórmula de Cálculo Utilizada ---------------------------------------------------------------------------------------

'''
Elasticidade = (% variação na quantidade vendida) / (% variação no preço)

Interpretação:
Elasticidade < -1: Demanda elástica → reduzir preço pode aumentar a receita
Elasticidade > -1: Demanda inelástica → aumentar preço pode aumentar a receita
Elasticidade ≈ 0: Produto indiferente ao preço → manter preço

'''

# ---------------------------------------------------------------------------------------------- Desenvolvimento --------------------------------------------------------------------------------------------'

# Cálculo da Elasticidade-Preço da Demanda
def calcular_elasticidade(grupo):
    grupo = grupo.sort_values(by='Semana')
    grupo['Pct_Δ_Preco'] = grupo['Preco'].pct_change()
    grupo['Pct_Δ_Volume'] = grupo['Volume'].pct_change()
    grupo['Elasticidade'] = grupo['Pct_Δ_Volume'] / grupo['Pct_Δ_Preco']
    return grupo

# Iterar por SKU
df_elast = df.groupby('SKU').apply(calcular_elasticidade).reset_index(drop=True)

# Elasticidade Média
elasticidade_media = (
    df_elast
    .replace([np.inf, -np.inf], np.nan)  # remover infinitos
    .groupby(['SKU', 'Categoria'])['Elasticidade']
    .mean()
    .reset_index(name='Elasticidade_Media')
)

# Condicional: Ação Sugerida
def sugerir_acao(e):
    if e < -1:
        return 'Reduzir preço'
    elif e > -1:
        return 'Aumentar preço'
    else:
        return 'Manter preço'

elasticidade_media['Acao_Sugerida'] = elasticidade_media['Elasticidade_Media'].apply(sugerir_acao)

# Exportar Resultado
elasticidade_media.to_excel(output, index=False)