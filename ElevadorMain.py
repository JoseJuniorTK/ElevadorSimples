import random
import os
import getch
import Core
import sys
import vlc
from termcolor import cprint

# Musicas a serem importadas
menu = vlc.MediaPlayer("./menu.mp3")
wait = vlc.MediaPlayer("./wait.mp3")
done = vlc.MediaPlayer("./done.mp3")
menu.play()

# Set de variaveis:

emprogresso = True
auto = True

# Listas para cada uma das funções
Intencao = [0, 0, 0, 0, 0, 0]
PessoasEmEspera = []
PessoasEmEsperaVisual = []
IntencaoVisual = []
PessoasDentro = [0, 0, 0, 0, 0, 0]
PessoasSairam = [0, 0, 0, 0, 0, 0]
elevador = [u"\u2800", u"\u2800", u"\u2800", u"\u2800", u"\u2800", u"\u2800"]
queue = [0, 0, 0, 0, 0, 0]
velocidade = 2
total = 0

# Valor a ser guardado de pessoas que já utilizaram.


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def Total(total):
    total = sum(PessoasSairam) + total
    print('Total de pessoas que já chegaram felizes a seus andares desde a 1 rodada:', '\033[92m', str(total), '\033[0m')


def Manual_Menu():
    print('')
    print('--------------------------------------------')
    print('             ##   Manual  ##')
    print('')
    print('E = Entrada de pessoas')
    print('D = Desejo (Onde quer ir)')
    print('Elev = Elevador')
    print('Saida = Quantas pessoas sairam em certo andar')
    print('')
    print('--------------------------------------------')
    print('            E-----D---Elev--Saida ')
    print('--------------------------------------------')
    print('           Pressione 1 Para voltar')


def Logo():
    print('  _____ _     _______     ___    ____   ___  ____  ')
    print(' | ____| |   | ____\ \   / / \  |  _ \ / _ \|  _ \ ')
    print(' |  _| | |   |  _|  \ \ / / _ \ | | | | | | | |_) | ')
    print(' | |___| |___| |___  \ V / ___ \| |_| | |_| |  _ < ')
    print(' |_____|_____|_____|  \_/_/   \_\____/ \___/|_| \_\ ')
    print('\033[93m', str('                                          Versão 0.5'), '\033[0m')


Logo()
cprint('         Pressione ENTER para começar.              ', 'yellow', attrs=['blink'])
iniciar = getch.getch()
while emprogresso is True:
    menu.pause()
    menu.play()
    if iniciar != '\n':
        cls()
        Logo()
        print('\033[93m', str('         Botao errado, pressione ENTER.              '), '\033[0m')
        iniciar = getch.getch()
    else:
        cls()
        Logo()
        print('                     MENU')
        print('Pressione as teclas para navegar pelo menu')
        print('[1] - Iniciar')
        print('[2] - Opções')
        print('[3] - Manual')
        print('[4] - Sair')
        if auto is True:
            print('\033[93m', '         Modo automatico ativado', '\033[0m')
        else:
            print('\033[93m', '        Modo manual ativado', '\033[0m')
        escolha = getch.getch()
        if escolha == '4':
            sys.exit()
        elif escolha == '3':
            natela = True
            while natela is True:
                cls()
                Logo()
                Manual_Menu()
                manual = getch.getch()
                if manual == '1':
                    natela = False
                else:
                    natela = True

        elif escolha == '2':
            natela = True
            while natela is True:
                cls()
                Logo()
                print('                  OPÇÕES')
                print('[1] - Velocidade da execução: ')
                print('[2] - Modo manual ou automatico.')
                print('[3] - Voltar')
                opcao = getch.getch()
                if opcao == '1':
                    cls()
                    Logo()
                    velocidade = int(input('Digite a nova velocidade: '))
                elif opcao == '2':
                    cls()
                    Logo()
                    print('[1] - Modo automatico [2] - Modo manual')
                    modo = getch.getch()
                    if modo == '1':
                        auto = True
                    elif modo == '2':
                        auto = False
                    else:
                        cls()
                        Logo()
                        print('Opção Invalida!')
                elif opcao == '3':
                    natela = False
        elif escolha == '1':
            # >>Engine do aparecimento de PessoasDentro<<
            # O laço vai repetir apenas 2x pra adicionar X PessoasDentro
            if auto is True:
                for i in range(5):
                    n = random.randint(1, 5)
                    # O numero de PessoasDentro em cada andar vai ser aleatorio
                    PessoasDentro[n] = random.randint(1, 3)
            # Caso a opção: automatico, seja desligada, a entrada de pessoas vai
            # ser manual.
            elif auto is False:
                cls()
                Logo()
                print('                  >POSICIONAMENTO<              ')

                p = int(input('Digite quantas pessoas em andares diferentes você irá colocar (Maximo 5): '))
                if p > 5 or p < 1 or p is None:
                    trava = True
                    while trava is True:
                        if p > 5 or p < 1 or p is None:
                            p = int(input('Limite invalido, Digite quantas pessoas '
                                          'diferentes em andares diferentes você '
                                          'irá colocar (Máximo 5): '))
                            trava = True
                        else:
                            trava = False
                else:
                    for i in range(p):
                        n = int(input('Digite o andar inicial da(s) pessoa(s) ' + str(i + 1) + ' (Máximo 5) : '))
                        if n > 5 or n < 1 or n is None:
                            trava = True
                            while trava is True:
                                if n > 5 or n < 1:
                                    n = int(input('Andar invalido. Digite o andar inicial da(s) pessoa(s) ' + str(i + 1) + ' (Máximo 5) : '))
                                    trava = True
                                else:
                                    trava = False
                        f = int(input('Digite quantas pessoas no andar ' + str(n) + ' vão entrar (Máximo 5): '))
                        if f > 5 or f < 1 or f is None:
                            trava = True
                            while trava is True:
                                if f > 5 or f < 1 or f is None:
                                    f = int(input('Numero invalido. Digite quantas pessoas no andar ' + str(n) + ' vão entrar (Máximo 5): '))
                                else:
                                    trava = False
                        PessoasDentro[n] = f
            # Visualiza
            PessoasEmEspera = PessoasDentro.copy()
            PessoasEmEsperaVisual = PessoasDentro.copy()
            # >>>Engine de intenções<<<
            # O laco vai percorrer a lista toda de 6 posições para pegar intenções
            if auto is True:
                for n2 in range(6):
                    # Se houver PessoasDentro neste andar, uma intenção aleatoria de 1 a 6 será
                    # gerada.
                    if PessoasDentro[n2] > 0:
                        # Bloco para identificar se a pessoa não vai para seu proprio andar.
                        naoigual = 0
                        # Enquanto a variavel não igual for 0
                        while naoigual == 0:
                            # Continuará mudando a variavel até ela ser diferente do andar que
                            # entrou.
                            Intencao[n2] = random.randint(1, 5)
                            if Intencao[n2] == n2:
                                naoigual = 0
                            # Sai do loop quando a condição se satisfazer.
                            else:
                                naoigual = 1
            # Faz o mesmo que o bloco anterior, porém manualmente.
            elif auto is False:
                for n2 in range(6):
                    if PessoasDentro[n2] > 0:
                        cls()
                        Logo()
                        print('                  >INTENCOES<              ')
                        Intencao[n2] = int(input('Para onde a pessoa no andar ' + str(n2) + ' vai?: '))
                        if Intencao[n2] == n2 or Intencao[n2] > 5 or Intencao[n2] < 0:
                            trava = True
                            while trava is True:
                                if Intencao[n2] == n2 or Intencao[n2] > 5 or Intencao[n2] < 0:
                                    trava = True
                                    Intencao[n2] = int(input('Desejo invalido, Para onde a pessoa no andar ' + str(n2) + ' vai?: '))
                                else:
                                    trava = False

            IntencaoVisual = Intencao.copy()
            menu.pause()
            wait.play()
            Core.Elevador(Intencao, PessoasEmEspera, PessoasEmEsperaVisual, IntencaoVisual, PessoasDentro, PessoasSairam, elevador, queue, velocidade)
            elevador = [u"\u2800", u"\u2800", u"\u2800", u"\u2800", u"\u2800", u"\u2800"]
            wait.stop()
            done.play()
            print('')
            print('            ***Execucao finalizada***')
            print('')
            total = sum(PessoasSairam) + total
            print('Total de pessoas que já chegaram felizes a seus andares desde o inicio:', '\033[92m', str(total), '\033[0m')
            print('')
            cprint('         Pressione ENTER para voltar ao MENU.              ', 'yellow', attrs=['blink'])
            input()
            done.stop()
            PessoasSairam = [0, 0, 0, 0, 0, 0]
