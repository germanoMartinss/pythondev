filmHarryPotter = {
    "title": "Harry Potter",
    "year": 2001,
    "imdbRating": 9.1,
    "genre": ["Fantasia", "Aventura", "Familia"],
}

print(filmHarryPotter)
print(len(filmHarryPotter))  # 4
print(type(filmHarryPotter))  # <class 'dict'>

# 1 - Recuperar um elemento do dicionário pelo nome da chave
print(filmHarryPotter["genre"]) # ["Fantasia", "Aventura", "Familia"]
print(filmHarryPotter.get("title")) # "Harry Potter"

# 2 - Buscar apenas as chaves do dicionário
print(filmHarryPotter.keys())  # dict_keys(['title', 'year', 'imdbRating', 'genre'])

# 3 - Buscar apenas os valores do dicionário
print(filmHarryPotter.values())  # dict_values(['Harry Potter', 2001, 9.1, ['Fantasia', 'Aventura', 'Familia']])

# 4 - Adicionar um item no dicionário
filmHarryPotter["director"] = "Chris Columbus"
print(filmHarryPotter)  # {'title': 'Harry Potter', 'year': 2001, 'imdbRating': 9.1, 'genre': ['Fantasia', 'Aventura', 'Familia'], 'director': 'Chris Columbus'}

# 5 - Buscar itens do dicionário com chave e valor
print(filmHarryPotter.items())  # dict_items([('title', 'Harry Potter'), ('year', 2001), ('imdbRating', 9.1), ('genre', ['Fantasia', 'Aventura', 'Familia']), ('director', 'Chris Columbus')])

# 6 - Atualizar um item do dicionário
filmHarryPotter.update({"year": 2002})
print(filmHarryPotter)  # {'title': 'Harry Potter', 'year': 2002, 'imdbRating': 9.1, 'genre': ['Fantasia', 'Aventura', 'Familia'], 'director': 'Chris Columbus'}

# 7 - Remover um item do dicionário
filmHarryPotter.pop("year")
print(filmHarryPotter)  # {'title': 'Harry Potter', 'imdbRating': 9.1, 'genre': ['Fantasia', 'Aventura', 'Familia'], 'director': 'Chris Columbus'}