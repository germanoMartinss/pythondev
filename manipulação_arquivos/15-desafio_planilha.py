import pandas as pd
import os
from pathlib import Path

# 1 - Importante os dados de  todas as sheets
tb_clientes_dict = pd.read_excel("manipulação_arquivos/dados/clientes.xlsx", sheet_name=None)
# print(tb_clientes_dict)

# 2 - Criando a pasta 'planilhas_separadas' se não existir
pasta_saida = 'manipulação_arquivos/dados/planilhas_separadas'
if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)

# 3 - Separando as planilhas
for nome_aba, tabela in tb_clientes_dict.items():
    caminho_arquivo = os.path.join(pasta_saida, f"{nome_aba}.xlsx")
    tabela.to_excel(caminho_arquivo, index=False)


# 4 Criando a pasta 'planilhas_consolidadas' se não existir
pasta_consolidadas = 'manipulação_arquivos/dados/planilhas_consolidadas'
if not os.path.exists(pasta_consolidadas):
    os.makedirs(pasta_consolidadas)

# 5 - Caminho para a planilha consolidada
caminho_planilha_consolidada = os.path.join(pasta_consolidadas, "planilha_consolidada.xlsx")

# 6 - Criando a planilha consolidada
with pd.ExcelWriter(caminho_planilha_consolidada) as consolidada:
    for arquivo in Path(pasta_saida).glob("*.xlsx"):
        tabela = pd.read_excel(arquivo)
        tabela.to_excel(consolidada, sheet_name=arquivo.stem, index=False)
