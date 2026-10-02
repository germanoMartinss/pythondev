"""
Fatorial de um número:
1 -> 1 * 1
2 -> 2 * 1
3 -> 3 * 2 * 1
4 -> 4 * 3 * 2 * 1
"""

# 1 - Fatorial de um número utilizando recursividade
def fatorial(n):
    if n == 1:
        return 1
    else:
        return (n * fatorial(n - 1))

number = int(input("Digite um número para calcular o fatorial:\n"))
print(f"O fatorial de {number} é: {fatorial(number)}")


# 2 - Soma total de um número utilizando recursividade
def soma_total(n):
    if n == 1:
        return 1
    else:
        return (n + soma_total(n - 1))

number = int(input("Digite um número para calcular a soma total:\n"))
print(f"A soma total de {number} é: {soma_total(number)}")