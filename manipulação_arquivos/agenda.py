import os

def add_contact():
    name = input("Informe o nome do contato:\n")
    phone = input("Informe o telefone do contato:\n")
    address = input("Informe o endereço do contato:\n")

    contact = f"Nome: {name}, Telefone: {phone}, Endereço: {address}\n"

    with open("manipulação_arquivos/dados/contacts.txt", "a", encoding='utf-8') as file:
        file.write(contact)

def view_contacts():
    if not os.path.exists("manipulação_arquivos/dados/contacts.txt"):
        print("A agenda está vazia.")
        return
    with open("manipulação_arquivos/dados/contacts.txt", "r", encoding='utf-8') as file:
        contacts = file.read()
    print("Lista de contatos:")
    print(contacts)

def delete_contacts():
    if not os.path.exists("manipulação_arquivos/dados/contacts.txt"):
        print("A agenda está vazia.")
        return
    with open("manipulação_arquivos/dados/contacts.txt", "w", encoding='utf-8') as file:
        file.write("")

    print("Contatos excluídos com sucesso.")