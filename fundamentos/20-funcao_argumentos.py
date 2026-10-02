# 1 - Função que imprime um nome completo

def full_name(first_name, last_name):
    print(f"Nome completo: {first_name} {last_name}")

full_name("João", "Silva")

# 2 - Função para somar dois números
def sum_numbers(num1, num2):
    return num1 + num2

print(f"A soma é: {sum_numbers(5, 3)}")

# 3 - Função com parametro default

def address(country="Brasil"): 
    print(f"País: {country}")

address()
address("Argentina")

# 4 - Função para avaliar um filme 
def rate_movie(num_ratings, movie_name):
    total = 0
    for i in range(num_ratings):
        note = float(input("Digite a nota do filme:\n"))
        total += note

    if num_ratings > 0:
        average = total / num_ratings
    else:
        average = 0

    print(f"A média de avaliações do filme {movie_name} é: {average:.2f}")

rate_movie(3, "Interstellar")