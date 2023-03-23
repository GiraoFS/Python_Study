import random


def imprimir_mensagem_abertura():
    print('*********************************')
    print('***Bem vindo ao jogo de Forca!***')
    print('*********************************')


def carregar_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def inicializar_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def solicitar_chute():
    chute = input('Qual letra você deseja tentar? ').strip().upper()
    return chute


def marcar_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1


def imprimir_mensagem_ganhador():
    print('Você ganhou!\n')


def imprimi_mensagem_perdedor():
    print('Você perdeu!\n')


def jogar():

    imprimir_mensagem_abertura()
    palavra_secreta = carregar_palavra_secreta()
    letras_acertadas = inicializar_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:
        chute = solicitar_chute()

        if chute in palavra_secreta:
            marcar_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        imprimir_mensagem_ganhador()
    else:
        imprimi_mensagem_perdedor()


if __name__ == "__main__":
    jogar()
