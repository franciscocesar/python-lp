"""
Iniciar com letra, pode conter números, esperar _, letras minúsculas
"""
nome = 'Francisco César'
idade = 32
altura = 1.80
e_maior = idade > 18
peso = 80


print(nome, type(nome))
print('Nome:', nome, 'Idade: ', idade, 'Altura', altura, 'É de maior: ', e_maior)
print(idade * altura)

print(peso/(altura ** 2))