import json

dados = {
    "clientes":[
        {"id": 1, "nome": "Germano", "idade": 35, "cidade": "Santos"},
        {"id": 2, "nome": "Ana", "idade": 28, "cidade": "Campinas"},
        {"id": 3, "nome": "Carlos", "idade": 42, "cidade": "Sorocaba"},
        {"id": 4, "nome": "Juliana", "idade": 31, "cidade": "Ribeirão Preto"},
        {"id": 5, "nome": "Rafael", "idade": 25, "cidade": "São José dos Campos"},
    ]
}

caminho_arquivo = "manipulação_arquivos/dados/clientes.json"

#1- Criando o arquivo json
with open(caminho_arquivo, 'w', encoding='utf-8') as file:
    json.dump(dados, file, indent=4)

#2- Lendo os dados do arquivo JSON
with open(caminho_arquivo, 'r', encoding='utf-8') as file:
    dados = json.load(file)
    print(dados)

#3- Manipulando dados
for cliente in dados["clientes"]:
    if cliente["nome"] == "Germano":
        cliente["idade"] = 37

novo_cliente = {"id": 6, "nome": "Fernanda", "idade": 31, "cidade": "Santos"}
dados["clientes"].append(novo_cliente)

#4- Salvar dados manipulados no arquivo
with open(caminho_arquivo, 'w', encoding='utf-8') as file:
    json.dump(dados, file, indent=4)