import argparse
import hashlib
import sys

parse = argparse.ArgumentParser()
parse.add_argument("-p", "--password", help="Pon aqui el hash de la password.", required=False)
parse.add_argument("-w", "--wordlist", help="Añade aqui el archivo del wordlist", required=True)
parse.add_argument("-a", "--archivo", help="Añade el fichero de usuario:contraseña", required=False)
parse.add_argument("-f", help="Añade el nombre del hash del cifrado(Admitidos: md5, sha1, sha256, sha512, blake2)", required=True)
args = parse.parse_args()

def check_hash():
    wordlist = args.wordlist
    word = open(wordlist, "r")
    pas = args.password
    for linea in word:
        contraseña = linea.strip()

        if args.f == "sha1":
            hash_dict = hashlib.sha1(contraseña.encode()).hexdigest()
        elif args.f == "md5":
            hash_dict = hashlib.md5(contraseña.encode()).hexdigest()
        elif args.f == "sha256":
            hash_dict = hashlib.sha256(contraseña.encode).hexdigest()
        elif args.f == "sha512":
            hash_dict = hashlib.sha512(contraseña.encode()).hexdigest()
        elif args.f == "blake2":
            hash_dict = hashlib.blake2b(contraseña.encode()).hexdigest()



        if pas == hash_dict:
            print(f'El hash: {args.password} es la palabra: {linea}')
            sys.exit()

    print("No esta en el wordlist, prueba con otro.")
    word.close()


check_hash()