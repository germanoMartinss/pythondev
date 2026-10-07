import csv

linguagem = input("Informe o nome da linguagem de programação: \n")
caterogia = input("Informe a categoria da linguagem de programação: \n")

with open('manipulação_arquivos/dados/cursos.csv', 'a', encoding='utf-8') as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerow([linguagem, caterogia])