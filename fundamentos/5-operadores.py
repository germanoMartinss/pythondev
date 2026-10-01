num1 = int(input("Digite o primeiro número:\n"))
num2 = int(input("Digite o segundo número:\n"))

sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
rest = num1 % num2
exp = num1 ** num2

print(f"A soma é {sum}")
print(f"A subtração é {sub}")
print(f"A divisão é {div:.2f}")
print(f"A multiplicação é {mult}")
print(f"O resto da divisão é {rest}")
print(f"A potência é {exp}")

# Comparação 
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
notEqual = num1 != num2
greaterOrEqual = num1 >= num2
lessOrEqual = num1 <= num2

print(f"O primeiro número é maior que o segundo número? {bigger}")
print(f"O primeiro número é menor que o segundo número? {smaller}")
print(f"O primeiro número é igual ao segundo número? {equal}")
print(f"O primeiro número é diferente do segundo número? {notEqual}")
print(f"O primeiro número é maior ou igual ao segundo número? {greaterOrEqual}")
print(f"O primeiro número é menor ou igual ao segundo número? {lessOrEqual}")

# Atribuição
num1 += 10
num1 -= 10
num1 *= 10
num1 /= 10

