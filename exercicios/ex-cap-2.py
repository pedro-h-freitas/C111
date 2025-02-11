from math import sqrt, ceil, floor, trunc

# 1. Crie um programa que leia seu nome completo e mostre:
# • Seu nome com todas as letras maiúsculas
# • Seu nome com todas as letras minúsculas
# • Quantas letras ao todo tem seu nome
# • E como seria se trocássemos seu último nome para “do Inatel”

print(f'{"="*10} Atividade 1 {"="*10}')

nome_completo = input("Insira seu nome completo: ")

print(f'Seu nome com todas as letras maiúsculas: {nome_completo.upper()}')
print(f'Seu nome com todas as letras minúsculas: {nome_completo.lower()}')
print(
    f'Quantas letras ao todo (com espaço) tem seu nome: {len(nome_completo)}'
)
print(
    f'Quantas letras ao todo (sem espaço) tem seu nome: {len(nome_completo.replace(' ', ''))}'
)

nome_split = nome_completo.split(' ')
nome_split[-1] = "do Inatel"

print(' '.join(nome_split))

# 2. Mostre a tabuada de um número que o usuário escolher dentro de um
# intervalo específico também escolhido por ele

print(f'{"="*10} Atividade 2 {"="*10}')

numero = int(input('Escolha um numero (inteiro): '))
comeco = int(input('Escolha o começo o intervalo: '))
fim = int(input('Escolha o fim o intervalo: '))

for i in range(comeco, fim+1):
    print(f'{numero}*{i}={numero*i}')

# 3. Faça um programa que leia o sexo de uma pessoa e diga se ela é
# homem (caso seja digitado M) ou mulher (caso seja digitado F). Caso
# seja digitado algo inválido, continue perguntando até que o usuário
# entre com um sexo válido

print(f'{"="*10} Atividade 3 {"="*10}')

d = {'M': 'homem', 'F': 'mulher'}

while True:
    sexo = input('Sexo (M)asculino ou (F)eminino: ')
    if sexo == 'M' or sexo == 'F':
        break
    print('\nValor inválido, apenas (M) ou (F)')

print(d[sexo])

# 4. Desenvolva um script que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$ 0.50 por Km para viagens até 200Km
# e R$ 0.45 para viagens mais longas

print(f'{"="*10} Atividade 4 {"="*10}')

distancia = float(input('Distancia (em KM): '))

valor = distancia * 0.5 if distancia <= 200 else distancia*0.45

print(f'Valor: R$ {valor:.2f}')

# 5. Faça um programa que leia um número entre 1000 e 9999 e mostre na tela
# • qual o número da unidade
# • número da dezena
# • número da centena
# • E número do milhar

print(f'{"="*10} Atividade 5 {"="*10}')

numero = int(input('Escolha um numero entre 1000 e 9999: '))

print(f'Unidade: {numero % 10}')
numero //= 10

print(f'Dezena: {numero % 10}')
numero //= 10

print(f'Centena: {numero % 10}')
numero //= 10

print(f'Milhar: {numero % 10}')

# 6. Peça ao usuário para entrar com um número decimal.
# Em seguida, aplique e mostre o resultado:
# • da raiz quadrada deste número
# • função teto
# • função chão
# • sua parte inteira

print(f'{"="*10} Atividade 6 {"="*10}')


numero = float(input('Escolha um numero decimal: '))

print(f"Raiz quadrada: {sqrt(numero)}")
print(f"Função teto: {ceil(numero)}")
print(f"Função chão: {floor(numero)}")
print(f"Parte inteira: {trunc(numero)}")
