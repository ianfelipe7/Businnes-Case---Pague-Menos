# 📊 Case 2 de Precificação — Pague Menos

**Processo Seletivo: Analista de Precificação Digital**

## 💡 Objetivo

Este projeto tem como objetivo analisar a sensibilidade ao preço dos produtos de uma rede de varejo farmacêutico, com base em dados históricos de vendas e preços. A partir dessa análise, o código recomenda ações de precificação que maximizem a receita da empresa.

---

## 📈 Metodologia

Utilizamos o conceito de **elasticidade-preço da demanda**, que mede o quanto a quantidade vendida de um produto varia em resposta a alterações no preço.

### Fórmula aplicada:
Elasticidade = (% variação na quantidade) / (% variação no preço)

yaml
Sempre exibir os detalhes

Copiar

### Interpretação:
- **Elasticidade < -1**: Demanda elástica → Reduzir preço
- **Elasticidade > -1**: Demanda inelástica → Aumentar preço
- **Elasticidade ≈ 0**: Produto indiferente ao preço → Manter preço

---

## ⚙️ Etapas do Código

1. **Leitura da base de dados histórica** (`Base de Dados_Case 2.csv`)
2. **Cálculo da elasticidade semanal por SKU**
3. **Cálculo da elasticidade média por produto**
4. **Geração da recomendação de precificação**
5. **Exportação do output em planilha (`Output_Case2_Precificacao.csv`)**

---

## 📁 Estrutura de Arquivos

├── Base de Dados_Case 2.csv # Base de dados histórica
├── Output_Case2_Precificacao.csv # Resultado final com recomendações
├── precificacao_case2.py # Código Python principal
└── README.md # Este arquivo

yaml
Sempre exibir os detalhes

Copiar

---

## ▶️ Como Executar

Você pode rodar este projeto em:

- [Google Colab](https://colab.research.google.com/)
- [Replit](https://replit.com/)
- Seu ambiente local com Python 3.x

### Requisitos:
```bash
pip install pandas numpy
📤 Output Esperado
A planilha final contém:

SKU	Categoria	Elasticidade_Media	Acao_Sugerida
SKU_1	Medicamento	-1.35	Reduzir preço
SKU_2	Medicamento	-0.75	Aumentar preço

🧠 Conclusão
Este modelo oferece uma abordagem quantitativa para tomada de decisão em precificação, promovendo um alinhamento entre valor percebido, demanda e receita.
"""
