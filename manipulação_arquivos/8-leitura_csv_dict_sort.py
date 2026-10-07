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

def get_language(curso):
    return curso["language"]

def get_category(curso):
    return curso["category"]

for curso in sorted(cursos, key=get_category):
    print(f"{curso['language']}-{curso['category']}")