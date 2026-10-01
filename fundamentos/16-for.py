# Lista de Filmes

movieList = ["Interstellar", "Exorcista", "O Poderoso Chefão", "A Origem", "O Senhor dos Anéis"]
print(movieList)

# 1 - Interando valores de uma lista com for
for movie in movieList:
    print(movie)

# 2 - Quando a condição for atendida, o loop é interrompido com break
for movie in movieList:
    if  movie == "O Poderoso Chefão":
        print(f"Filme encontrado: {movie}")
        break

# 3 - Quando a condição for atendida, o loop é interrompido com continue
for movie in movieList:
    if  movie == "O Poderoso Chefão":
        print(f"Filme encontrado: {movie}")
        continue
    print(f"Filme não encontrado: {movie}")

# 4 - Avaliação do filme

movieName = input("Digite o nome do filme: ")
movieRating = int(input("Digite quantas avaliações deseja fazer: \n"))

total = 0
for i in range(movieRating):
    rating = float(input(f"Digite a nota da avaliação:\n "))
    total += rating

if movieRating > 0:
    averageRating = total / movieRating
    print(f"A média das avaliações do filme {movieName} é: {averageRating}")
else:
    averageRating = 0
    print(f"A média das avaliações do filme {movieName} é: {averageRating}")