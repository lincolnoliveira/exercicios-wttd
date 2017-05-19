#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Problem description:
# https://developers.google.com/edu/python/exercises/copy-special


import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise

"""

def get_special_paths(dir):
    """
Gather a list of the absolute paths of the special files in all the directories.
A "special" file is one where the name contains the pattern __w__ somewhere, where the w is one or more word chars.
"""
    padrao=r'.*__\w*__.*'
    arqs=os.listdir(dir)
    final=[]
    for arquivo in arqs:
        if re.search(padrao,arquivo):
            final.append(arquivo)

    return final

def copy_to(paths, dir):
    #copy the files to the given directory, creating it if necessary
    print('Copiar ',paths, ' para ', dir)
    if not (os.path.exists(dir)):
        os.mkdir(dir)

    for arq in paths:
        shutil.copy(arq, dir)

    return

def zip_to(paths, zippath):
    # run this command: "zip -j zipfile <list all the files>". This will create a zipfile containing the files.
    # Just for fun/reassurance, also print the command line you are going to do first
    # If the child process exits with an error code, exit with an error code and print the command's output
    print('Zipar ', paths, ' para ', zippath)
    comando = 'zip -j '+ zippath
    larg = ['zip','-j', zippath]
    for arq in paths:
        comando += ' '+arq
        larg.append(arq)

    print('Comando: '+comando)

    r=subprocess.run(args=larg, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    if (r.returncode):
        print ('Comando executado com erro!')
        print (r.returncode)
        print (r.stdout)

    return r.returncode

def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)

    for dir in args:
        paths= get_special_paths(dir)
        if todir:
            copy_to(paths, todir)

        if tozip:
            return zip_to(paths, tozip)

if __name__ == "__main__":
    main()
