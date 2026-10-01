movieName = "Harry Potter"
movieDescription = """
    Harry Potter é uma série de livros de fantasia escrita pela autora britânica J.K. Rowling. 
A história segue as aventuras do jovem bruxo Harry Potter e seus amigos Hermione Granger e Ron Weasley, 
que frequentam a Escola de Magia e Bruxaria de Hogwarts. A série é composta por sete livros, 
que foram adaptados para uma série de filmes de sucesso. A história aborda temas como amizade, 
coragem, amor e a luta entre o bem e o mal, enquanto Harry enfrenta o vilão Lord Voldemort e 
descobre seu próprio destino como o "Menino que Sobreviveu". A série de Harry Potter se tornou um fenômeno cultural, 
conquistando fãs em todo o mundo e influenciando a literatura infantojuvenil, além de gerar uma vasta gama de produtos derivados, 
incluindo jogos, brinquedos e parques temáticos. 
"""

print(movieName.upper())  # HARRY POTTER
print(movieName.lower())  # harry potter
print(movieName.capitalize())  # Harry potter
print(movieName.title())  # Harry Potter
print(movieName.center(20, "-"))  # ----Harry Potter-----
print(movieName.find("a")) # 1
print(movieName.find("o")) # 6
print(movieName.replace("Harry Potter", "Harry Potter e a Pedra Filosofal")) # Altera elemento da string