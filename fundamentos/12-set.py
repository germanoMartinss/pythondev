filmsSet = {
    "Interstellar", "Exorcista", "O Poderoso Chefão", "A Origem", "O Senhor dos Anais"
}

print(type(filmsSet))  # <class 'set'>

# 1 - Tamanho do conjunto de filmes
print(len(filmsSet))  # 5

# 2 - Adicionar um item no conjunto de filmes
filmsSet.add("Matrix")
print(filmsSet)  # {"Interstellar", "Exorcista", "O Poderoso Chefão", "A Origem", "O Senhor dos Anais", "Matrix"}

# 3 - Remover um item do conjunto de filmes
filmsSet.remove("Matrix")
print(filmsSet)  # {"Interstellar", "Exorcista", "O Poderoso Chefão", "A Origem", "O Senhor dos Anais"}

# 4 - True e 1 são considerados o mesmo valor
exemploSet = {"Interstellar", True, 1, 8.5}
print(exemploSet) # {"Interstellar", True, 8.5}

# 5 - Adicionar item de outro set 
filmsSet.update(exemploSet)
print(filmsSet) 

# 6 - Remover um item do set
filmsSet.discard(8.5)
filmsSet.discard(True)

# 7 - Limpar o conjunto de filmes
filmsSet.clear()
print(filmsSet)  # set()