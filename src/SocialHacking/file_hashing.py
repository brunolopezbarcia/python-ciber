import argparse
import hashlib

import os
import sys

parse = argparse.ArgumentParser()
parse.add_argument('-a', '--file', required=False)
parse.add_argument('-c', '--folder', required=False)
parse.add_argument('-f', '--hash', required=True)
parse.add_argument('-v', '--version', required=False)

args = parse.parse_args()

def hasher(file):

    with open(file, 'rb') as fil:
        if args.hash == 'md5':
            print(hashlib.md5(fil.read()).hexdigest() + ' -- ' + file + ' -- '+ args.hash)
        elif args.hash == 'sha1':
            print(hashlib.sha1(fil.read()).hexdigest() + ' -- ' + file + ' -- '+ args.hash)
        elif args.hash == 'sha256':
            print(hashlib.sha256(fil.read()).hexdigest() + ' -- ' + file + ' -- '+ args.hash)
        elif args.hash == 'sha512':
           print(hashlib.sha512(fil.read()).hexdigest() + ' -- ' + file + ' -- '+ args.hash)
        elif args.hash == "blake2":
            print(hashlib.blake2b(fil.read()).hexdigest() + ' -- ' + file + ' -- '+ args.hash)
        else:
            print("Tipo de hash Invalido")

def main():
    if args.file != None:
        hasher(args.file)
    elif args.folder != None:
        for archivo in os.listdir(args.folder):
            if os.path.isdir(args.folder + archivo):
                print("Es un directorio -- " + archivo)
            else:
                hasher(args.folder + archivo)
    elif args.v != None:
        print("1.0")
    else:
        print("Argumentos Invalidos")

main()