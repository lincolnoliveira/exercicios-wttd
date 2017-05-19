#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib.request
import shutil

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""

    def ultima_palavra(url):
        expressao=r'-([a-z]+)\.jpg'
        return re.search(expressao,url).group(1)

    arquivo = open(filename,'r')

    #Sim: 10.254.254.28 - - [06/Aug/2007:00:06:15 -0700] "GET /edu/languages/google-python-class/images/puzzle/p-bigg-bbgg.jpg HTTP/1.0" 302 5694 "-" "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
    #Não: 10.254.254.29 - - [06/Aug/2007:00:13:29 -0700] "GET /keyser/24760/ HTTP/1.0" 200 3404 "-" "googlebot-mscrawl-moma (enterprise; bar-XYZ; foo123@google.com,foo123@google.com,foo123@google.com,foo123@google.com)"

    expressao= r'(\/edu[\/a-zA-Z0-9.\-]*jpg) HTTP'

    lista = []

    for linha in arquivo:
        s = re.search(expressao,linha)
        if s:
           url = s.group(1)
    #       print (url)
    #       print (ultima_palavra(url))
           if not 'http://code.google.com'+url in lista:
               lista.append('http://code.google.com'+url)


    #print (lista)
    lista.sort(key=ultima_palavra)
    #print(lista)

    return lista

def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    os.chdir(dest_dir)

    indice = open('index.html','w')

    indice.write('<verbatim>\n<html>\n<body>\n')

    cont=0
    for url in img_urls:
        #resposta = urllib.request.urlopen('http://code.google.com'+url)
        #arquivo = open('img'+str(cont))
        #shutil.copyfileobj(resposta,arquivo)
        print (cont)
        print (url)
        urllib.request.urlretrieve(url, 'img'+str(cont))
        indice.write('<img src="img'+str(cont)+'">')
        cont += 1

    indice.write('</body>\n</html> ')
    indice.close()


def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile ')
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print('\n'.join(img_urls))


if __name__ == '__main__':
    main()
