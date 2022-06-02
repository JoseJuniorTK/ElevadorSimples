# ElevadorSimples
Projeto final de disciplina de programação 1 em Python - Universidade Federal do Pará\
**Desenvolvido por:** José Maria Junior Lopes Perdigão. - 2019

**Para utilizar apenas instale os requirements necessários e rode o ElevadorMain.py, testado apenas em sistemas UNIX (Linux)**
**Caso a musica não funcione, instale o reprodutor multimidia VLC em seu computador**

**Estruturação do código:**

**ElevadorMain.py** chama a função principal do nucleo da aplicação, responsável por criar a tela inicial e manter o código rodando.

**Core.py** é o nucleo da aplicação, a logica principal do elevador está neste arquivo.

**Logica do código:** \
1 - O código gera um grupo de pessoas aleatoriamente por andar, cada grupo tem sua intenção de ir para um determinado andar.\
2 - A pessoa só entrará no elevador se ele estiver indo para o andar que ela deseja, se a pessoa quiser ir para o segundo e o elevador estiver cheio e subindo, a pessoa só vai entrar no elevador quando o elevador descer.\
3 - O elevador para em determinado andar quando não houver mais pessoas utilizando-o.
