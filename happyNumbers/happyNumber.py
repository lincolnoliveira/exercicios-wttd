"""
Os números felizes são definidos pelo seguinte procedimento. 

Começando com qualquer número inteiro positivo, o número é substituído pela soma dos quadrados 
dos seus dígitos, e repetir o processo até que o número seja igual a 1 
ou até que ele entre num ciclo infinito que não inclui um 
ou seja a soma dos quadrados dos algarismos do quadrado de um número positivo inicial. 

Os números no fim do processo de extremidade com 1, são conhecidos como números feliz, 
mas aqueles que não terminam com um 1 são números chamados infelizes.

7 é um número feliz:
72 = 49 
42 + 92 = 97 
92 + 72 = 130 
12 + 32 + 02 = 10 
12 + 02 = 1. 

Se  não é feliz, a soma dos quadrados nunca dará 1, serão gerados infinitos termos.
4, 16, 37, 58, 89, 145, 42, 20, 4, ... 
"""

def happy(num):
    testados = []
    while num != 1 and not num in testados:
        testados.append(num)
        num = sum ([int(digito) ** 2 for digito in str(num)])

        # o código acima corresponde a:

        # digitos_ao_quadrado = []
        # for digito in str(num):
        #     digitos_ao_quadrado.append(int(digito) ** 2)
        # num = 0
        # for digito in digitos_ao_quadrado:
        #     num += digito

    return num == 1;

# versão recursiva
def happy_rec(num):
    if num < 7:
        return num == 1 # condição de parada, sabendo que 1 é o único feliz abaixo de 7 e todos acabarão chegando a um nº < 7
    return happy_rec(sum ([int(digito) ** 2 for digito in str(num)]))
# inline if
# return num == 1 if num < 7 else happy_rec(sum ([int(digito) ** 2 for digito in str(num)]))


# versão interativa usando a mesma condição de parada da recursiva
def happy_int(num):
    while num >= 7:
        num = sum ([int(digito) ** 2 for digito in str(num)])
    return num == 1;


assert all(happy(n) for n in (1, 10, 100, 130, 7))
assert all(not happy(n) for n in (2,3,4,5,6,8,9,11))

assert all(happy_rec(n) for n in (1, 10, 100, 130, 7))
assert all(not happy_rec(n) for n in (2,3,4,5,6,8,9,11))

assert all(happy_int(n) for n in (1, 10, 100, 130, 7))
assert all(not happy_int(n) for n in (2,3,4,5,6,8,9,11))
