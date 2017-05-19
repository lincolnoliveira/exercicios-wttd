"""
http://dojopuzzles.com/problemas/exibe/analisando-a-conjectura-de-collatz/
https://projecteuler.net/index.php?section=problems&id=14
Para definir uma seqüência a partir de um número inteiro o positivo, temos as seguintes regras:

n → n/2 (n é par)

n → 3n + 1 (n é ímpar)

Usando a regra acima e iniciando com o número 13, geramos a seguinte seqüência:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

Podemos ver que esta seqüência (iniciando em 13 e terminando em 1) contém 10 termos. 
Embora ainda não tenha sido provado (este problema é conhecido como Problema de Collatz), 
sabemos que com qualquer número que você começar, a seqüência resultante chega no número 1 
em algum momento.

Desenvolva um programa que descubra qual o número inicial entre 1 e 1 milhão que produz a maior seqüência.
"""

conhecidos = {1:1}  # para guardar termos conhecidos e evitar repeticao de chamadas a proximo

calculos = 0        # não é necessário para o algoritmo. É só para compararmos as duas soluções

# Para max = 1.000,     a implementação sem historico usa      59.542 "cálculos", a com histórico usa     2.227 (3,7%).
#                                                     rodou em 0.020s           , a com historico rodou em 0.001s (5%%). - 0.001 talvez seja o mínimo que mostra...
# Para max = 1.000.000, a implementação sem historico usa 131.434.424 "cálculos", a com histórico usa 2.168.610 (1,6%)
#                                                     rodou em 43.5s            , a com historico rodou em 1.5s (3,4%).


def proximo(n):
    '''
    :param n: número atual
    :return: próximo número de acordo com a sequencia de Collatz
    '''
    global calculos
    calculos += 1
    if (n % 2 == 0):
        return n // 2
    else:
        return 3 * n + 1


def termos(n):
    '''
    :param n: número a ser testado 
    :return: quantos termos para chegar a 1
    '''
    if n in conhecidos:
        return conhecidos.get(n)
    else:
        result = 1 + termos(proximo(n))
        conhecidos[n] = result
        return result

def termos_sem_historico(n):
    '''
    :param n: número a ser testado 
    :return: quantos termos para chegar a 1
    '''
    if n == 1:
        return 1
    else:
        return 1 + termos_sem_historico(proximo(n))


def maior_sequencia(max):
    '''
    :param max: número limite a ser testado 
    :return: maior numero de termos gerados para números entre 1 e max
    '''
    maior = 0
    encontrado = 0
    for i in range(1, max+1):
        atual = termos(i)
        if maior < atual:
            maior = atual
            encontrado = i
    print('Cálculos = ', calculos)
    print ('Para números até {}, o número com a maior sequência encontrado foi {}, com {} termos.'.format(max, encontrado, maior))
    return encontrado