movieName = "Top Gun"
movieName2 = "top Gun"

print(movieName == movieName2)  # False

movieDescription = """Top Gun: Maverick é um filme de ação e drama de 2022 dirigido por Joseph Kosinski. 
É a sequência do filme Top Gun de 1986, estrelado por Tom Cruise como o piloto de caça Pete 'Maverick' Mitchell. 
O filme segue Maverick enquanto ele treina uma nova geração de pilotos da Marinha dos Estados Unidos, 
incluindo o filho de seu falecido amigo e co-piloto, Goose. O filme recebeu elogios da crítica e foi um sucesso de bilheteria, 
arrecadando mais de US$ 1,4 bilhão em todo o mundo.
"""

print(movieName)
# 1 - Multiplicação de string
line = "="
print(line*50)
print(movieDescription)

# 2 - Procurar uma palavra na string
print("Marinha" in movieDescription)
print("Germano" in movieDescription)
print("Gun" in movieName)