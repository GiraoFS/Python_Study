from jogo_adivinhacao import adivinhacao
from jogo_forca import forca


def escolher_jogo():
    print('*********************************')
    print('********Escolha seu jogo!********')
    print('*********************************\n')

    print('[1] - Forca | [2] - Adivinhação\n')

    jogo = int(input('Informe qual jogo deseja jogar conforme opções acima: '))

    if jogo == 1:
        print('Iniciar Forca\n')
        forca.jogar()
    elif jogo == 2:
        print('Iniciar Adivinhação\n')
        adivinhacao.jogar()

if __name__ == "__main__":
    escolher_jogo()