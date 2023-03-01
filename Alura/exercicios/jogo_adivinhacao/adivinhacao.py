print('*********************************')
print('Bem vindo ao jogo de Adivinhação!')
print('*********************************')

numero_secreto = 27
total_de_tentativas = 3

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
        print('Você acertou!\n')
        break
    else:
        if chute_maior:
            print('Você errou! O seu chute foi maior que o número secreto.\n')
        elif chute_menor:
            print('Você errou! O seu chute foi menor que o número secreto.\n')

print('Fim do jogo!')
