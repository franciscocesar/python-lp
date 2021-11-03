"""
Entrada de dados
"""
nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

ano_nascimento = 2019 - idade
print(f'O usuário digitou {nome}, sua idade é: {idade} e nasceu em: {ano_nascimento}')

numero_1 = float(input('Digite um numero'))
numero_2 = float(input('Digte outro numero '))

adicao = numero_1 + numero_2

print(f'A soma de {numero_1} é {numero_2} é: {adicao} ')