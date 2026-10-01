filmesLista = ["Interstellar", "Exorcista", "O Poderoso Chefão", "A Origem", "O Senhor dos Anéis"]



# 1 - Tamanho da lista de filmes
print(len(filmesLista))  # 5

# 2 - Recuperar um item pelo índice da lista de filmes pelo nome
print(filmesLista.index("O Poderoso Chefão"))  # 2

# 3 - Adicionar um item na lista de filmes
filmesLista.append("Matrix")
print(filmesLista)  # ["Interstellar", "Exorcista", "O Poderoso Chefão", "A Origem", "O Senhor dos Anéis", "Matrix"]

# 4 - Ordernar a lista de filmes em ordem alfabética
filmesLista.sort()
print(filmesLista)  # ["A Origem", "Exorcista", "Interstellar", "Matrix", "O Poderoso Chefão", "O Senhor dos Anéis"]

# 5 - Copiar os itens da lista de filmes para uma nova lista
novaListaFilmes = filmesLista.copy()
print(novaListaFilmes)  # ["A Origem", "Exorcista", "Interstellar", "Matrix", "O Poderoso Chefão", "O Senhor dos Anéis"]

# 6 - Remover um item da lista de filmes
filmesLista.remove("Matrix")
print(filmesLista)  # ["A Origem", "Exorcista", "Interstellar", "O Poderoso Chefão", "O Senhor dos Anéis"]

# 7 - Limpar a lista de filmes
filmesLista.clear()
print(filmesLista)  # []