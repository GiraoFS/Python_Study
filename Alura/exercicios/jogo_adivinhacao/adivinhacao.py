import random

def jogar():
    print('*********************************')
    print('Bem vindo ao jogo de Adivinhação!')
    print('*********************************\n')

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print('Qual o nível de dificuldade desejado?')
    print('[1] Fácil - [2] Médio - [3] Difícil')

    nivel = int(input('Defina o nível: '))

    while nivel < 1 or nivel > 3:
        print('Você deve escolher entre os níveis indicados: [1] Fácil - [2] Médio - [3] Difícil')
        nivel = int(input('Defina o nível: '))

    if nivel == 1:
        total_de_tentativas = 20
        print(f'Nível escolhido: Fácil. Você tem {total_de_tentativas} chances.\n')
    elif nivel == 2:
        total_de_tentativas = 10
        print(f'Nível escolhido: Médio. Você tem {total_de_tentativas} chances.\n')
    else:
        total_de_tentativas = 5
        print(f'Nível escolhido: Difícil. Você tem {total_de_tentativas} chances.\n')

    for rodada in range(1, total_de_tentativas + 1):
        print(f'Tentativa: {rodada}/{total_de_tentativas}.')

        chute = int(input('Digite um número entre 1 e 100: '))
        print(f'Você digitou {chute}.\n')

        if chute < 1 or chute > 100:
            print('Você deve digitar um número entre 1 e 100. Você perdeu essa rodada.\n')
            continue

        acertou = chute == numero_secreto
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto

        if acertou:
            print(f'Você acertou! Sua pontuação é {pontos}!\n')
            break
        else:
            if chute_maior:
                print('Você errou! O seu chute foi maior que o número secreto.\n')
                if rodada == total_de_tentativas:
                    print(f'O número secreto era: {numero_secreto}!\n')
            elif chute_menor:
                print('Você errou! O seu chute foi menor que o número secreto.\n')
                if rodada == total_de_tentativas:
                    print(f'O número secreto era: {numero_secreto}!\n')

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print('Fim do jogo!')

if __name__ == "__main__":
    jogar()
