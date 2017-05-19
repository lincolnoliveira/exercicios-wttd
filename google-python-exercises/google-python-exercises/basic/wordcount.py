#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.


2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

# Define print_words(filename) and print_top(filename) functions.

"""

import sys
import collections

# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

def frequencia_palavras(filename):
    """Retorna um dicionário com as palavras e o numero de vezes que ocorrem"""
    arquivo = open(filename,'r')
    stringao = arquivo.read()
    stringao=stringao.lower()
    dicionario = {}
    for chave in stringao.split():
        if chave in dicionario:
            dicionario[chave] += 1
        else:
            dicionario[chave]=1
    return dicionario

""""
1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.
"""
def print_words(filename):
    dicionario=frequencia_palavras(filename)
    chaves= list(dicionario.keys());
    chaves.sort();
    for k in chaves:
        print(k+":"+str(dicionario[k]))

    # outro modo usando collections

    ordenado= collections.OrderedDict(sorted(dicionario.items()))
    print (ordenado)

    return

def print_top(filename):
    dicionario=frequencia_palavras(filename)

    listaOrdenada = list(dicionario.items())  # cria uma lista de tuplas dos itens do dict

    def valor(tupla):
        return tupla[1]  # retorna o segundo item da tupla, o primeiro (0) é a chave, já que a tupla veio de um item de dicionario

    listaOrdenada.sort(key=valor,reverse=True)

    cont=0
    for i in listaOrdenada:
        print('Key: {0} \t Value: {1}'.format(i[0], i[1]))
        cont += 1
        if cont > 10:
            break

    # resposta da internet, basicamente o funcionamento acima em uma linha
    ordenado = collections.OrderedDict(sorted(dicionario.items(), key=lambda t: t[1], reverse=True))  # lambda t:t[1], uma função implícita que vai retornar o valor (t[1]) para cada item

    cont=0
    for k, v in ordenado.items():
        print('Key: {0} \t Value: {1}'.format(k, v))
        cont += 1
        if cont > 10:
            break
    return

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
