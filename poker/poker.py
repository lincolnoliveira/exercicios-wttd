'''
No jogo de Poker, uma mão consiste em cinco cartas que podem ser comparadas, da mais baixa para a mais alta, da seguinte maneira:

    Carta Alta: A carta de maior valor.
    Um Par: Duas cartas do mesmo valor.
    Dois Pares: Dois pares diferentes.
    Trinca: Três cartas do mesmo valor e duas de valores diferentes.
    Straight (seqüência): Todas as cartas com valores consecutivos.
       - usamos a regra que o Ás só pode ser usado como mais alto (deuce-to-seven low rules)
    Flush: Todas as cartas do mesmo naipe.
    Full House: Um trinca e um par.
    Quadra: Quatro cartas do mesmo valor.
    Straight Flush: Todas as cartas são consecutivas e do mesmo naipe.
    Royal Flush: A seqüência 10, Valete, Dama, Rei, Ás, do mesmo naipe.

    As cartas são, em ordem crescente de valor: 2, 3, 4, 5, 6, 7, 8, 9, 10, Valete (J), Dama (Q), Rei (K), Ás (A).
    Os naipes são: Ouro (D), Copa (H), Espadas (S), Paus (C)

Se dois jogadores possuem a mesma mão, vence que tiver a mão formada pelas cartas de maior valor.

Alguns exemplos de mão e seus respectivos vencedores:

Jogador 1              Jogador 2              Vencedor
5H 5C 6S 7S KD         2C 3S 8S 8D TD         
Par de cinco           Par de oito            Jogador 2

5D 8C 9S JS AC         2C 5C 7D 8S QH         
Carta mais alta: Ás    Carta mais alta: Dama  Jogador 1

2D 9C AS AH AC         3D 6D 7D TD QD         
Trinca de Ás           Flush com Ouro         Jogador 2

4D 6S 9H QH QC         3D 6D 7H QD QS         
Par de Damas           Par de Damas           
Carta mais alta: 9     Carta mais alta: 7     Jogador 1

2H 2D 4C 4D 4S         3C 3D 3S 9S 9D         
Full House             Full House             
Com três 4             Com três 3             Jogador 1


Desenvolva um programa que, de acordo com as mãos de dois jogadores, informe qual deles é o vencedor.

'''

ordemCartas = "234567891JQKA"


def valorCarta(carta):
    '''
    retorna o "valor" da carta, sendo 2 a mais baixa (2) e 14 a mais alta (ás) -- começa em 2 para ser mais intuitivo
    :param carta: representação da carta, string, o primeiro ou os dois primeiros chars representam o número/figura e o último char o naipe
    :return:   valor da carta
    '''
    return ordemCartas.find(carta[0]) + 2 # primeira [0] letra


def listaValoresOrdenados(listaCartas, decrescente=False):
    '''
     Retorna uma lista ordenada com os valores das cartas recebidas
    :param listaCartas: lista de cartas no formato conhecido, em qualquer ordem
    :return: lista ordenada com os valores das cartas recebidas
    '''
    ordenada = []
    for carta in listaCartas:
        ordenada.append(valorCarta(carta))
    ordenada.sort(reverse=decrescente)
    return ordenada


def rank(listaCartas):
    '''
     O ranking de um conjunto de cartas envolve todas as suas cartas, considerando as mais altas primeiro
    :param listaCartas: lista de cartas no formato conhecido, em qualquer ordem
    :return: valor que expresse ordenadamente o flush considerando a a ordem da mais alta para a mais baixa
    '''
    ordenada = listaValoresOrdenados(listaCartas)
    rank = 0
    multiplicador = 1
    for valor in ordenada:
        rank += valor * multiplicador
        multiplicador *= 100 # a cada carta seu valor é 100x maior que a anterior, para ficar fácil de visualizar o valor de cada carta no rank
    return rank

def rankFullHouse(grupos):
    '''
    :param grupos: dicionário na forma {'Quadra':qtos, 'Trinca':qtos, 'Par1':qtos, 'Par2':qtos}
    :return: um ranking que serve para comparar em relação ao full house 
    '''
    if grupos['Trinca'] > 0 and grupos['Par1'] > 0:
        return grupos['Trinca'] * 100 + grupos['Par1']
    return 0

def rank2pares(grupos):
    '''
    :param grupos: dicionário na forma {'Quadra':qtos, 'Trinca':qtos, 'Par1':qtos, 'Par2':qtos}
    :return: um ranking que serve para comparar em relação a 2 pares 
    '''
    if grupos['Par1'] > 0 and grupos['Par2'] > 0:
        return grupos['Par1'] * 100 + grupos['Par2']
    return 0


def straight(listaCartas):
    """
    Identifica e rankeia o straight (sequencia de cartas consecutivas) numa lista de cartas.
    O ranking do straight é o valor de sua carta mais alta
    :param listaCartas: lista de cartas no formato conhecido, em qualquer ordem
    :return: 0 qdo não tem straight, valor da carta mais alta quando tem
    """
    ordenada = listaValoresOrdenados(listaCartas)
    anterior = ordenada[0]
    for valor in ordenada[1:]:
        if valor != anterior + 1:
            return 0
        anterior = valor

    return ordenada[-1]


def flush(listaCartas):
    '''
    Identifica e rankeia o flush (todas as cartas do mesmo naipe)
    :param listaCartas: lista de cartas no formato conhecido, em qualquer ordem
    :return: 0 quando não tem flush, rank() do flush qdo tem
    '''
    naipe = listaCartas[0][-1] # último char da primeira carta
    for carta in listaCartas[1:]:
        if carta[-1] != naipe:
            return 0
    return rank(listaCartas)

def gruposCartas(listaCartas):
    '''
    Identifica os grupos de cartas com mesmo valor, retornando um dicionário com os grupos 
    :param listaCartas: listaCartas: lista de cartas no formato conhecido, em qualquer ordem
    :return: dicionário na forma {'Quadra':qtos, 'Trinca':qtos, 'Par1':qtos, 'Par2':qtos}
    '''
    grupos = {'Quadra':0, 'Trinca':0, 'Par1':0, 'Par2':0}
    ordenada = listaValoresOrdenados(listaCartas,True)
    # acrescenta 0, que não é um valor válido, no final da lista para forçar o teste dentro do loop; senão teria que fazer todos os testes no fim do loop de novo
    ordenada.append(0)
    repetidos = 1
    anterior = ordenada[0]
    for atual in ordenada[1:]:
        if anterior == atual:
            repetidos += 1
        else:
            if repetidos == 4:
                grupos['Quadra'] = anterior
            elif repetidos == 3:
                grupos['Trinca'] = anterior
            elif repetidos == 2:
                if grupos['Par1'] == 0:
                    grupos['Par1'] = anterior
                else:
                    grupos['Par2'] = anterior

            repetidos = 1
            anterior = atual


    return grupos

def comparaMaos(mao1, mao2):

    # straight flush
    f1 = flush(mao1)
    f2 = flush(mao2)
    s1 = straight(mao1)
    s2 = straight(mao2)
    sf1 = s1 * f1     # se algum dos dois não é aplicável, a multiplicação será 0
    sf2 = s2 * f2     # o maior valor necessariamente é o maior straight flush, já que serão sequencias
    if sf1 > sf2:
        return 1
    elif sf1 < sf2:
        return 2

    # quadra
    g1 = gruposCartas(mao1)
    g2 = gruposCartas(mao2)
    if g1['Quadra'] > g2['Quadra']:
        return 1
    elif g1['Quadra'] < g2['Quadra']:
        return 2

    # full house
    fh1 = rankFullHouse(g1)
    fh2 = rankFullHouse(g2)
    if fh1 > fh2:
        return 1
    elif fh1 < fh2:
        return 2

    # flush
    if f1 > f2:
        return 1
    elif f1 < f2:
        return 2

    # straight
    if s1 > s2:
        return 1
    elif s1 < s2:
        return 2

    # trinca
    if g1['Trinca'] > g2['Trinca']:
        return 1
    elif g1['Trinca'] < g2['Trinca']:
        return 2

    # 2 pares
    dp1 = rank2pares(g1)
    dp2 = rank2pares(g2)
    if dp1 > dp2:
        return 1
    elif dp1 < dp2:
        return 2

    # 1 par
    if g1['Par1'] > g2['Par1']:
        return 1
    elif g1['Par1'] < g2['Par1']:
        return 2

    # mais alta
    v1 = rank(mao1)
    v2 = rank(mao2)
    if v1 > v2:
        return 1
    elif v1 < v2:
        return 2
    else:
        return 0