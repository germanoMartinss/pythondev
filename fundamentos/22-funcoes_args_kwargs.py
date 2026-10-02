"""
*args - Utilizamos ele quando não temos certeza de quantos argumentos
serão passados para uma função. 
- Eles sempre serão passados como tuplas

**kwargs - Utilizamos ele quando temos certeza de quantos argumentos
serão passados para uma função. 
- Eles sempre são passados como dicionários
"""

# 1 - Soma de números
def sum(*num):
    total = 0
    for n in num:
        total += n
    print(f"A soma de {num} é: {total}")

sum(1, 2, 3, 4, 5)
sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
sum(24, 25)

# 2 - Apresentação de curso
def presentation(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

presentation(name="João", age=20, course="Python")