filmsTuple = ("Interstellar", "Exorcista", "O Poderoso Chefão", "A Origem", "O Senhor dos Anéis")

print(type(filmsTuple))  # <class 'tuple'>

# 1 - Buscar os 2 primeiros filmes da tupla de filmes
print(filmsTuple[:2])  # Interstellar, Exorcista

# 2 - Buscar o último filme da tupla de filmes
print(filmsTuple[-1])  # O Senhor dos Anéis

# 3 - Buscar até uma posição específica da tupla de filmes
print(filmsTuple[:3])  # Interstellar, Exorcista, O Poderoso Chefão

# 4 - Buscar filmes de uma posição específica até o final da tupla de filmes
print(filmsTuple[2:5])  # O Poderoso Chefão, A Origem, O Senhor dos Anéis

# 5 - Tamanho da tupla de filmes
print(len(filmsTuple))  # 5

# 6 - Recuperar um item pelo índice da tupla de filmes pelo nome
print(filmsTuple.index("O Poderoso Chefão"))  # 2