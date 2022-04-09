import random

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while (x < min) or (x > max):
        x = int(input(pergunta))
    return x

def vencedor(jogador1, jogador2):
    global empate, v1, v2
    if jogador1 == 1:
        if jogador2 == 1: #pedra x #pedra
            empate += 1
            print('Empate')
        elif jogador2 == 2: #pedra x papel
            v2 += 1
            print('Você perdeu')
        elif jogador2 == 3: #pedra x tesoura
            v1 += 1
            print('Você ganhou')

    elif jogador1 == 2:
        if jogador2 == 1: #papel x pedra
            v1 += 1
            print('Você ganhou')
        elif jogador2 == 2: #papel x papel
            empate += 1
            print('Empate')
        elif jogador2 == 3: #papel x tesoura
            v2 += 1
            print('Você perdeu')

    elif jogador1 == 3:
        if jogador2 == 1: #tesoura x pedra
            v2 += 1
            print('Você perdeu')
        elif jogador2 == 2: #tesoura x papel
            v1 += 1
            print('Você ganhou')
        elif jogador2 == 3: #tesoura x tesoura
            empate += 1
            print('Empate')
    resultados = [v1, v2, empate]
    return resultados

#programa principal

print('PEDRA, PAPEL E TESOURA')
print('1 - Pedra, 2 - Papel, 3 - Tesoura, 0 - Sair')

resultados = []
jogadas = []
v1 = 0
v2 = 0
empate = 0

while True:
    j1 = valida_int('Escolha sua jogada: ', 0, 3)
    if j1 == 0:
        print('Encerrando o programa')
        break
    j2 = random.randint(1, 3)
    jogadas.append([j1, j2])
    resultados = vencedor(j1, j2)
    for jogada in jogadas:
        for dado in jogada:
            print(dado, end=' ')
        print()

print('Vitórias do Jogador 1: {}'.format(resultados[0]))
print('Vitórias do Jogador 2: {}'.format(resultados[1]))
print('Empates: {}'.format(resultados[2]))