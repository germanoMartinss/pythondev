"""
Arquivos - Modos de Operação

1 -> Modo W - write
2 -> Modo R - read
3 -> Modo A - append
"""

with open("manipulação_arquivos/dados/names.txt", "r", encoding='utf-8') as file:
    # print(file.read())
    for line in file:
        print(f"Olá, {line.rstrip()}!")