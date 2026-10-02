# 1 - listar valores de 0 a 10 que sejam menores do que 4 
listNumbers = [ i for i in range(10) if i < 4 ]
print(listNumbers)

# Lista de filmes 
movieList = ["Interstellar", "Exorcista", "O Poderoso Chefão", "A Origem", "O Senhor dos Anéis"]

# 2 - Filmes que possuem a letra "e" no título
movieWithE = [ movie for movie in movieList if "e" in movie.lower() ]
print(movieWithE)

# 3 - Filmes que eu já assisti 
moviesWatched = [ movie for movie in movieList if movie != "O Poderoso Chefão" ]
print(moviesWatched)

# 4 - Encontrando um filme pelo nome
while True:
    movieName = input("Digite o nome do filme para buscar na lista (ou sair para encerrar):\n ")
    if movieName.lower() == "sair":
        print("Encerrando a busca de filmes.")
        break
    
    movieFound = [ movie for movie in movieList if movieName.lower() in movie.lower() ]
    if movieFound:
        print(f"Filme encontrado com o nome {movieFound}")
        for movie in movieFound:
            print(f"Filme encontrado: {movie}")
            break
    else:
        print("Filme não encontrado, tente novamente.")