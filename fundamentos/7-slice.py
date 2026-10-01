movieName = "Harry Potter"

# string[inicio:fim] - indice começa na posição 8 | indice final - 1

# 1 - Buscar toda a string a partir da primeira posição 
print(movieName[0:])  # Harry Potter

# 2 - Buscar toda a string a partid da última posição
print(movieName[:7])  # Harry P

# 3 - Buscar toda a string da terceira até a última posição
print(movieName[2:])  # rry Potter

# 4 - Buscar toda a string da terceira até a penúltima posição
print(movieName[3:-1])  # ry Pott

"""
string[inicio:fim:passo] - indice começa na posição 8 | indice final - 1  
passo - determina o incremento do índice, ou seja, quantos caracteres serão pulados a cada iteração
"""

# 5 - Buscar toda a string da terceira até a penúltima posiçao pulando de 2 em 2
print(movieName[::2])  # HryPte

# 6 - Buscar toda a string da terceira até a penúltima posiçao pulando de 3 em 3
print(movieName[::3])  # HryP

# 7 - Buscar toda a string nos indices impares
print(movieName[1::2])  # raPto

# 8 - Inverter uma string de trás para frente
print(movieName[::-1])  # rettoP yrraH