"""
fizzbuzz:
- quando múltiplo de 3, responde fizz
- quando múltiplo de 5, responde buzz
- quando múltiplo de 3 e 5, responde fizzbuzz
- senão, responde o número de entrada
"""

from functools import partial

# def eh_multiplo_de(testado, base):
#     return (testado % base) == 0

eh_multiplo_de = lambda testado, base: testado % base == 0

# inútil, só pra aprender o conceito mesmo
eh_multiplo_de_5 = partial(eh_multiplo_de,base=5)

def robot(i):
    retorno = str(i);
    if eh_multiplo_de(i, 15):
        retorno = 'fizzbuzz'
    elif eh_multiplo_de(i, 3):
        retorno = 'fizz'
    elif eh_multiplo_de_5(i):
        retorno = 'buzz'
    return retorno

"""
Teste inicial, sem o fw unittest

def self.assertEqual(testado, esperado):
    from sys import _getframe
    caller = _getframe().f_back
    linha = caller.f_lineno

    msg= 'Falha na linha {}: esperado {}, obtido {}'
    if not testado == esperado:
        print (msg.format(linha, esperado, testado))


if __name__ == '__main__':
    self.assertEqual(robot(1),'1')
    self.assertEqual(robot(2),'2')
    self.assertEqual(robot(4),'4')

    self.assertEqual(robot(3),'fizz')
    self.assertEqual(robot(6),'fizz')
    self.assertEqual(robot(12),'fizz')

    self.assertEqual(robot(5),'buzz')
    self.assertEqual(robot(10),'buzz')
    self.assertEqual(robot(20),'buzz')

    self.assertEqual(robot(15),'fizzbuzz')
    self.assertEqual(robot(30),'fizzbuzz')

"""