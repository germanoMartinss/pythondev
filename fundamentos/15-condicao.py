# Informações sobre o filme

name = input("Digite o nome do filme: \n")
yearRelease = int(input("Digite o ano do filme: \n"))
rating = float(input("Digite a nota do filme: \n"))

# Verificar se o filme é bom ou ruim com base na nota
if rating > 8.0 and yearRelease > 2000:
    print(f"O filme {name} é bom!")
else:
    print(f"O filme {name} é ruim!")