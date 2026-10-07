import pandas as pd
import numpy as np


dados_aba1 = {
    "ID": [1, 2, 3, 4, 5],
    "Nome": ["João", "Maria", "Pedro", "Ana", "Carlos"],
    "Idade": [25, 30, 35, 28, 4],
    "Cidade": ["Rio de Janeiro", "São Paulo", "Belo Horizonte", "Salvador", "Porto Alegre"]
}

dados_aba2 = {
    "ID": [6, 7, 8, 9, 10],
    "Nome": ["Fernanda", "Lucas", "Juliana", "Rafael", "Beatriz"],
    "Idade": [22, 41, 33, 29, 37],
    "Cidade": ["Curitiba", "Recife", "Fortaleza", "Manaus", "Florianópolis"]
}

dados_aba3 = {
    "ID": [11, 12, 13, 14, 15],
    "Nome": ["Gabriel", "Camila", "Thiago", "Larissa", "Bruno"],
    "Idade": [45, 26, 31, 39, 24],
    "Cidade": ["Goiânia", "Belém", "Vitória", "Natal", "Campo Grande"]
}

dados_aba4 = {
    "ID": [16, 17, 18, 19, 20],
    "Nome": ["Patrícia", "Eduardo", "Mariana", "Felipe", "Letícia"],
    "Idade": [34, 27, 42, 30, 23],
    "Cidade": ["João Pessoa", "Maceió", "Teresina", "Aracaju", "Cuiabá"]
}

df_aba1 = pd.DataFrame(dados_aba1)
df_aba2 = pd.DataFrame(dados_aba2)
df_aba3 = pd.DataFrame(dados_aba3)
df_aba4 = pd.DataFrame(dados_aba4)

caminho_arquivo = "manipulação_arquivos/dados/clientes.xlsx"

with pd.ExcelWriter(caminho_arquivo, engine='openpyxl') as writer:
    df_aba1.to_excel(writer, sheet_name='Aba1', index=False)
    df_aba2.to_excel(writer, sheet_name='Aba2', index=False)
    df_aba3.to_excel(writer, sheet_name='Aba3', index=False)
    df_aba4.to_excel(writer, sheet_name='Aba4', index=False)