cursos = []


with open("manipulação_arquivos/dados/cursos.csv", "r", encoding='utf-8') as file:
    for line in file:
        linha = line.rstrip().split(",")
        # print(f"{linha[0]} - {linha[1]}")
        linguagem, categoria = line.rstrip().split(",")
        cursos.append(f"{linguagem} - {categoria}")

for curso in sorted(cursos):
    print(curso)