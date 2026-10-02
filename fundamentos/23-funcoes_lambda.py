# Função de potência de um número

power = lambda num: num ** 2

print(power(6))

# Função que verifica se o número é par

is_even = lambda num: num % 2 == 0

print(is_even(6))
print(is_even(7))

# Função que divide um número por outro

divide = lambda num1, num2: num1 / num2

print(divide(10, 2))

# Função que inverte uma string

invert_string = lambda string: string[::-1]

print(invert_string("Python"))
print(invert_string("Programação"))

# Funcionalidades relacionadas aos filmes:
movieList = ["Interstellar", "Exorcista", "O Poderoso Chefão", "A Origem", "O Senhor dos Anéis"]
movieRatings = {
    "Interstellar": [8.6, 8.7, 8.8, 8.9, 9.0],
    "Exorcista": [6.5, 8.7, 7.1, 8.9, 9.9],
    "O Poderoso Chefão": [1.4, 2.3, 3.9, 4.1, 4.2],
    "A Origem": [8.7, 8.8, 8.9, 9.0, 9.1],
    "O Senhor dos Anéis": [9.0, 9.1, 9.2, 9.3, 9.4]
}

# Função para calcular a média de avaliações
movieRatingsAverage = lambda movie: sum(movieRatings[movie]) / len(movieRatings[movie])
print(f"A média de avaliações do filme Interstellar é: {movieRatingsAverage('Interstellar'):.2f}")

# Ordenar a lista de filmes em ordem alfabética
movieList.sort(key=lambda movie: movie.lower())
print(movieList)

# Ordenar a lista de filmes em ordem de média de avaliações do maior para o menor
movieList.sort(key=movieRatingsAverage, reverse=True)
print(f"lista de filmes em ordem de média de avaliações do maior para o menor: {movieList}")

# Ordenar a lista de filmes em ordem de média de avaliações do menor para o maior
movieList.sort(key=movieRatingsAverage)
print(f"lista de filmes em ordem de média de avaliações do menor para o maior: {movieList}")

# Função que verifica se o filme está na lista
check_movie = lambda movie: movie in movieList
print(check_movie("A Origem"))

# Função para recomendar um filme com base na média de avaliações
recommend_movie = lambda movie: f"Recomendamos o filme {movie} com a média de avaliações de {movieRatingsAverage(movie):.2f}"
print(recommend_movie("A Origem"))

