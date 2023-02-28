print('*********************************')
print('Bem vindo ao jogo de Adivinhação!')
print('*********************************')

numero_secreto = 27
total_de_tentativas = 3
rodada = 1

while rodada <= total_de_tentativas:
    print(f'Tentativa: {rodada}/{total_de_tentativas}.')
    chute = int(input('Digite o seu número: '))
    print(f'Você digitou {chute}.')

    acertou = chute == numero_secreto
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto

    if acertou:
        print('Você acertou!\n')
    else:
        if chute_maior:
            print('Você errou! O seu chute foi maior que o número secreto.\n')
        elif chute_menor:
            print('Você errou! O seu chute foi menor que o número secreto.\n')

    rodada += 1

print('Fim do jogo!')
