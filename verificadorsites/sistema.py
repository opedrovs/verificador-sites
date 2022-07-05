from verificadorsites.lib.interface import *
from verificadorsites.lib.arquivo import *
from verificadorsites.lib.ferramentas import *


while True:
    menu('VERIFICADOR DE SITES')
    print(f"""{amarelo}1{limpar} - {azul}Ver lista Sites
{amarelo}2{limpar} - {azul}Adicionar
{amarelo}3{limpar} - {azul}Remover
{amarelo}4{limpar} - {azul}Verificar conexão dos sites
{amarelo}5{limpar} - {azul}Sair do Programa{limpar}""")
    opc = leiaInt('Opção: ')
    if opc == 1:
        menu('LISTA SITES')
        verLista()
    elif opc == 2:
        menu('ADICIONAR')
        nome = input('Nome do Site: ')
        url = input('URL Completa: ')
        adicionarLista(nome, url)
    elif opc == 3:
        menu('REMOVER')
        verLista()
        nome = input('Nome do Site: ')
        removerLista(nome)
    elif opc == 4:
        menu('VERIFICAR CONEXÃO')
        verificarConexao()
    elif opc == 5:
        menuCarregando()
        menu('Saindo do Programa... Volte sempre!')
        break
    else:
        print(f'{vermelho}Opção inválida! Tente novamente!{limpar}')
