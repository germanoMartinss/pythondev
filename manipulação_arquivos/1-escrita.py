name = input("Digite o nome do aluno:\n")

"""
Arquivos - Modos de Operação

1 -> Modo W - write
2 -> Modo R - read
3 -> Modo A - append
"""

# Implementação 1 
# file = open("manipulação_arquivos/dados/names.txt", "a", encoding='utf-8')
# file.write(f"{name}\n")
# file.close()

# Implementação 2
with open("manipulação_arquivos/dados/names.txt", "a", encoding='utf-8') as file:
    file.write(f"{name}\n")
