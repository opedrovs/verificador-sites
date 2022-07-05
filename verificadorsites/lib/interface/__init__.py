from verificadorsites.decoracoes.cores import *


def menuCarregando():
    from time import sleep
    print(''.center(20), end='')
    for cont in range(1, 10):
        if cont <= 3:
            print(f'{verde}º', end='')
            sleep(0.5)
        elif cont <= 6:
            print(f'{amarelo}º', end='')
            sleep(0.5)
        elif cont <= 9:
            print(f'{vermelho}º{limpar}', end='')
            sleep(0.5)
    print()


def menu(txt):
    linha()
    print(txt.center(50))
    linha()


def linha():
    print('-' * 50)
