cursos = []


with open("manipulação_arquivos/dados/cursos.csv", "r", encoding='utf-8') as file:
    for line in file:
        linha = line.rstrip().split(",")
        # print(f"{linha[0]} - {linha[1]}")
        linguagem, categoria = line.rstrip().split(",")
        curso = {}
        curso["language"] = linguagem
        curso["category"] = categoria
        cursos.append(curso)

# print(cursos)



for curso in sorted(cursos, key=lambda curso: curso['language']):
    print(f"{curso['language']}-{curso['category']}")