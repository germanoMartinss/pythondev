# Lista de Filmes

movieList = ["Interstellar", "Exorcista", "O Poderoso Chefão", "A Origem", "O Senhor dos Anéis"]

# 1 - Interando valores de uma lista com while
index = 0
while index < len(movieList):
    print(movieList[index])
    index += 1

# 2 - Quando a condição for atendida, o loop é interrompido com break
index = 0
while index < len(movieList):
    if  movieList[index] == "O Poderoso Chefão":
        print(f"Filme encontrado: {movieList[index]}")
        break
    index += 1

# 3 - Quando a condição for atendida, o loop é interrompido com continue
index = 0
while index < len(movieList):
    if  movieList[index] == "O Poderoso Chefão":
        print(f"Filme encontrado: {movieList[index]}")
        index += 1
        continue
    print(f"Filme não encontrado: {movieList[index]}")
    index += 1

# 4 - Avaliação do filme

movieName = input("Digite o nome do filme: ")
movieRating = int(input("Digite quantas avaliações deseja fazer: \n"))

total = 0
index = 0
while index < movieRating:
    rating = float(input(f"Digite a nota da avaliação:\n "))
    total += rating
    index += 1

average = total / movieRating
print(f"A nota do filme {movieName} é {average}")
