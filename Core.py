# Arquivo contento a logica do elevador.
# Inicie-o no programa principal por um IMPORT.
import os
import time


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def Manual(queue):
    print('E-----D---Elev--Saida ')
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
    print('Desejos na lista de espera: ', str(queue))
    

def Elevador(Intencao, PessoasEmEspera, PessoasEmEsperaVisual, IntencaoVisual, PessoasDentro, PessoasSairam, elevador, queue, velocidade):
    # >>>Engine do elevador<<<
    # Elevador vai subir caso hajam pessoas.
    for n3 in range(6):
        PodeParar = False
        # Bloquinho de funcionamento grafico do elevador.
        elevador[n3] = u"\u2587"
        elevador[n3 - 1] = u"\u2800"
        cls()
        for h in reversed(range(6)):
            print(str(PessoasEmEsperaVisual[h]), u'\u25C6'u'\u25C6'u'\u25C6',
                  str(IntencaoVisual[h]), u'\u250B'u'\u250B'
                  '\033[32m', str(elevador[h]), '\033[0m'u'\u250B'u'\u250B',
                  str(PessoasSairam[h]))
        Manual(queue)
        time.sleep(velocidade)
        # Verificador se tem alguém esperando no andar..
        if int(Intencao[n3]) > 0 and Intencao[n3] > n3:
            PessoasEmEsperaVisual[n3] = 0
            temp1 = Intencao[n3]
            queue[n3] = temp1
            Intencao[n3] = 0
        # Se tiver, ele pega a intencao da pessoa e a coloca no lugar
        # desejado, se houverem mais pessoas saindo nesse andar, elas serao
        # somadas.
        if PessoasSairam[n3] == 0:
            total = 0
            for n4 in range(len(queue)):
                if int(queue[n4]) == n3 and n3 != 0:
                    temp = queue[n4]
                    total = PessoasEmEspera[n4] + total
                    PessoasSairam[temp] = total
                    PessoasEmEspera[n4] = 0
                    queue[n4] = 0
        # Se houver pessoas que sairam neste andar, ele pega e soma elas.             
        elif PessoasSairam[n3] != 0:
            total = 0
            for n4 in range(len(queue)):
                if int(queue[n4]) == n3 and n3 != 0:
                    temp = queue[n4]
                    total = PessoasEmEspera[n4] + total + PessoasEmEspera[n3]
                    PessoasSairam[temp] = total
                    PessoasEmEspera[n4] = 0
                    queue[n4] = 0
        # Caso o numero de pessoas em espera seja 0, ele para a execução.
        if sum(PessoasEmEspera) == 0:
            PodeParar = True
        cls()
        if PodeParar is True:
            cls()
            for h in reversed(range(6)):
                print(str(PessoasEmEsperaVisual[h]), u'\u25C6'u'\u25C6'u'\u25C6',
                      str(IntencaoVisual[h]), u'\u250B'u'\u250B'
                      '\033[91m', str(elevador[h]), '\033[0m'u'\u250B'u'\u250B',
                      str(PessoasSairam[h]))
            Manual(queue)
            time.sleep(velocidade)
            break
    # Se ainda houverem pessoas esperando após a subida, desça.
    if sum(PessoasEmEspera) != 0:
      for n3 in reversed(range(6)):
        # Bloquinho de funcionamento grafico do elevador.
        elevador[n3] = u"\u2587"
        if n3 < 5:
            elevador[n3 + 1] = u"\u2800"
        cls()
        for h in reversed(range(6)):
            print(str(PessoasEmEsperaVisual[h]), u'\u25C6'u'\u25C6'u'\u25C6',
                  str(IntencaoVisual[h]), u'\u250B'u'\u250B'
                  '\033[32m', str(elevador[h]), '\033[0m'u'\u250B'u'\u250B',
                  str(PessoasSairam[h]))
        Manual(queue)
        time.sleep(velocidade)
        # Verificador se tem alguem esperando no andar.
        if int(Intencao[n3]) > 0 and Intencao[n3] < n3:
            PessoasEmEsperaVisual[n3] = 0
            temp1 = Intencao[n3]
            queue[n3] = temp1
            Intencao[n3] = 0
        # Se tiver, ele pega a intencao da pessoa e a coloca no lugar
        # desejado.
        if PessoasSairam[n3] == 0:
            total = 0
            for n4 in range(len(queue)):
                if int(queue[n4]) == n3 and n3 != 0:
                    temp = queue[n4]
                    total = PessoasEmEspera[n4] + total
                    PessoasSairam[temp] = total
                    PessoasEmEspera[n4] = 0
                    queue[n4] = 0
        elif PessoasSairam[n3] != 0:
            total = 0
            for n4 in range(len(queue)):
                if int(queue[n4]) == n3 and n3 != 0:
                    temp = queue[n4]
                    total = PessoasEmEspera[n4] + total + PessoasEmEspera[n3]
                    PessoasSairam[temp] = total
                    PessoasEmEspera[n4] = 0
                    queue[n4] = 0
        if sum(PessoasEmEspera) == 0:
            PodeParar = True 
       # Esse bloco para o laco caso ele já possa parar.
        if PodeParar is True:
            cls()
            for h in reversed(range(6)):
                print(str(PessoasEmEsperaVisual[h]), u'\u25C6'u'\u25C6'u'\u25C6',
                      str(IntencaoVisual[h]), u'\u250B'u'\u250B'
                      '\033[91m', str(elevador[h]), '\033[0m'u'\u250B'u'\u250B',
                      str(PessoasSairam[h]))
            Manual(queue)
            time.sleep(velocidade)
            break
