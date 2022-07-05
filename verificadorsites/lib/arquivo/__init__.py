from verificadorsites.decoracoes.cores import *


def verLista():
    print(f'{"Nome do Site":<18}{"URL"}')
    try:
        with open('lista.txt', 'r', encoding='utf-8') as arquivo:
            texto = arquivo.read()
            print(texto)
    except:
        with open('lista.txt', 'a+', encoding='utf-8') as arquivo:
            texto = arquivo.read()
            print(texto)


def adicionarLista(nome, url):
    with open('lista.txt', 'a+', encoding='utf-8') as arquivo:
        arquivo.write(f'{nome:<18}{url}\n')
    print(f'{verde}Site {amarelo}{nome} {verde}adicionado na lista com sucesso!{limpar}')


def removerLista(nome):
    with open('lista.txt', 'r+', encoding='utf-8') as arquivo:
        novo_arq = arquivo.readlines()
        arquivo.seek(0)
        for line in novo_arq:
            if nome not in line:
                arquivo.write(line)
            else:
                print(f'{verde}Site {amarelo}{nome} {verde}removido da lista com sucesso!{limpar}')
        arquivo.truncate()


def verificarConexao():
    import urllib.request
    with open('lista.txt', 'r+', encoding='utf-8') as arquivo:
        texto = arquivo.read().split()
        for link in range(0, len(texto)):
            if link % 2 == 1:
                nome_site = link - 1
                try:
                    site = urllib.request.urlopen(texto[link])
                except Exception as e:
                    print(f'{vermelho}Conexão do site {amarelo}{texto[nome_site]} {vermelho}com problemas: {e}{limpar}')
                else:
                    print(f'{verde}Conexão do site {amarelo}{texto[nome_site]} {verde}com sucesso!{limpar}')
