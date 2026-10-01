import pprint

filmDict = { 
    "Harry Potter": {
        "year": 2001,
        "imdbRating": 9.1,
        "genre": ["Fantasia", "Aventura", "Familia"],
    },
    "Interstellar": {
        "year": 2014,
        "imdbRating": 8.6,
        "genre": ["Ficção Científica", "Drama", "Aventura"],
    },
    "O Poderoso Chefão": {
        "year": 1972,
        "imdbRating": 9.2,
        "genre": ["Crime", "Drama"],
    }
}

print(filmDict)

# 1 - Utilizando pprint para imprimir o dicionário de forma mais legível
pprint.pprint(filmDict)

# 2 - Buscar uma informação dentro do dicionário aninhado
print(filmDict["Harry Potter"]["year"])  # 2001

# 3 - Buscar o gênero do filme "Interstellar"
print(filmDict["Interstellar"]["genre"])  # ["Ficção Científica", "Drama", "Aventura"]

# 4 - Adicionar novo item
filmDict["Harry Potter"]["director"] = "Chris Columbus"
print(filmDict["Harry Potter"])  # {'year': 2001, 'imdbRating': 9.1, 'genre': ['Fantasia', 'Aventura', 'Familia'], 'director': 'Chris Columbus'}

# 5 - Remover um item 
del filmDict["Harry Potter"]["director"]
print(filmDict["Harry Potter"])  # {'year': 2001, 'imdbRating': 9.1, 'genre': ['Fantasia', 'Aventura', 'Familia']}

# 6 - Adicionar um novo filme ao dicionário
filmDict["A Origem"] = {
    "year": 2010,
    "imdbRating": 8.8,
    "genre": ["Ficção Científica", "Ação", "Aventura"],
}
print(filmDict["A Origem"])  # {'year': 2010, 'imdbRating': 8.8, 'genre': ['Ficção Científica', 'Ação', 'Aventura']}

"""
Criando uma lista de compras
"""

prodDisc = {
    "Arroz": 15.50,
    "Feijão": 8.90,
    "Macarrão": 6.75
}


# 1 - Imprimir o dicionário de produtos
print(prodDisc)

# 2 - Buscando o produto mais caro
print(max(prodDisc, key=prodDisc.get))  # Arroz

# 3 - Como buscar a média de preço dos produtos
print(sum(prodDisc.values()) / len(prodDisc))