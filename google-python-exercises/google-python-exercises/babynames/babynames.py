#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import collections

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename, summary):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]

    """
    arquivo = open(filename,'r')
    lista=[]
    dic={}

    # <tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>


#    Sintaxe mais comum, separa os grupos () e acessa depois pelo ordinal - 1, 2, 3
#    regNomes = r'<td>(\d*)</td><td>([A-Za-z]*)</td><td>([A-Za-z]*)</td>'

#   Sintaxe mais sofisticada, nomeia os grupos. ?P após o ( indica que agora vem uma extensão python das RE; no caso o que vem entre <> é o nome do grupo
    regNomes = r'<td>(?P<pos>\d*)</td><td>(?P<boy>[A-Za-z]*)</td><td>(?P<girl>[A-Za-z]*)</td>'

    for linha in arquivo:
        # <h3 align="center">Popularity in 1990</h3>
        if re.search('Popularity in ',linha):
            regAno='[0-9]{4}'
            lista.append(re.search(regAno,linha).group())

        s = re.search(regNomes, linha)
        if re.search(regNomes,linha):
            pos= s.group('pos')   # ou s.group(1)
            boy= s.group('boy')   # ou s.group(2)
            girl= s.group('girl')   # ou s.group(3)
            dic[boy]=pos
            dic[girl]=pos

    ordenado= collections.OrderedDict(sorted(dic.items()))

    for k, v in ordenado.items():
        lista.append(k+" "+v)

    if summary:
        arquivo= open('sumario.txt','w')
        for item in lista:
            arquivo.write(item+'\n')
        arquivo.close()
    else:
        print(lista)
    return


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    # For each filename, get the names, then either print the text output
    # or write it to a summary file

    for arq in args:
        extract_names(arq, summary)

if __name__ == '__main__':
    main()
