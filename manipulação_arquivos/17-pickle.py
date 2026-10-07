import pickle

class Cliente:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def __str__(self):
        return f"{self.nome} {self.idade} anos - {self.cidade}"

clientes = [
    Cliente("Germano", 35, "Santos"),
    Cliente("Ana", 28, "Campinas"),
    Cliente("Carlos", 42, "Sorocaba")
]

# Salvar lista de cliente em arquivos pickle
with open("manipulação_arquivos/dados/clientes.pk1", "wb") as f:
    pickle.dump(clientes, f)

# Carregando os dados de um arquivo pickle
with open("manipulação_arquivos/dados/clientes.pk1", "rb") as f:
    clientes = pickle.load(f)

for cliente in clientes:
    print(cliente)

# Adicionar cliente

novo_cliente = Cliente("Fernanda", 31, "Santos")
clientes.append(novo_cliente)

with open("manipulação_arquivos/dados/clientes.pk1", "wb") as f:
    pickle.dump(clientes, f)