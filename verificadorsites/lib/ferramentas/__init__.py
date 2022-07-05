from verificadorsites.decoracoes.cores import *


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print(f'{vermelho}ERRO: Valor inválido! Tente novamente!{limpar}')
        else:
            num = int(n)
            return num
