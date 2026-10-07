import xml.etree.ElementTree as ET

dados = """<?xml version='1.0' encoding='utf-8'?>
<clientes>
    <cliente>
        <id>1</id>
        <nome>Germano</nome>
        <idade>35</idade>
        <cidade>Santos</cidade>
    </cliente>
    <cliente>
        <id>2</id>
        <nome>Fernanda</nome>
        <idade>28</idade>
        <cidade>Rio de Janeiro</cidade>
    </cliente>
    <cliente>
        <id>3</id>
        <nome>Carlos</nome>
        <idade>42</idade>
        <cidade>Sorocaba</cidade>
    </cliente>
</clientes>
"""

caminho_arquivo = "manipulação_arquivos/dados/clientes.xml"

#1-Exportando dados para xml
with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write(dados)

#2-Lendo dados do xml
tree = ET.parse(caminho_arquivo)
root = tree.getroot()

for cliente in root.findall("cliente"):
    id_cliente = cliente.find("id").text
    nome_cliente = cliente.find("nome").text
    idade_cliente = cliente.find("idade").text

    print(f"Id: {id_cliente} -> Nome: {nome_cliente}")