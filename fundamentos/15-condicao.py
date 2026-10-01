# Informações sobre o filme

name = input("Digite o nome do filme: \n")
yearRelease = int(input("Digite o ano do filme: \n"))
rating = float(input("Digite a nota do filme: \n"))

# Verificar se o filme é bom ou ruim com base na nota
if rating > 8.0 and yearRelease > 2000:
    print(f"O filme {name} é bom!")
else:
    print(f"O filme {name} é ruim!")


num1 = float(input("Digite o primeiro número: \n"))
num2 = float(input("Digite o segundo número: \n"))
operation = input("Digite a operação desejada (+, -, *, /): \n")

if operation == "+":
    result = num1 + num2
    print(f"O resultado da soma é: {result}")
elif operation == "-":
    result = num1 - num2
    print(f"O resultado da subtração é: {result}")
elif operation == "*":
    result = num1 * num2
    print(f"O resultado da multiplicação é: {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"O resultado da divisão é: {result}")
    else:
        print("Erro: Divisão por zero não é permitida.")    
else:
    print("Operação inválida. Por favor, digite uma operação válida (+, -, *, /).")