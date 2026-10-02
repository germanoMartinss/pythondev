# 1 - Função para imprimir uma mensagem 

def welcome():
    print("Bem-vindo ao sistema de filmes!")

# for i in range(3):
#     welcome()

# 2 - Função para calcular a média de notas
def calcular_media():
    num_ratings = int(input("Digite o número de avaliações: "))
    total = 0
    for i in range(num_ratings):
        rating = float(input(f"Digite a avaliação: "))
        total += rating

    if num_ratings > 0:
        average = total / num_ratings
    else:
        average = 0

    return average


print(f"a média de avaliações é: {calcular_media():.2f}") # calcular_media()

# 3 - Função para cadastrar um filme
def cadastrar_filme():
    name = input("Digite o nome do filme:\n")
    yearLaunch = int(input("Digite o ano de lançamento:\n"))
    noteMovie = float(input("Digite a nota do filme:\n"))
    print(f"Filme cadastrado: {name}, Ano: {yearLaunch}, Nota: {noteMovie}")

cadastrar_filme()