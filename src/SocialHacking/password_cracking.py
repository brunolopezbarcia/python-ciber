import argparse
import hashlib
import sys

parse = argparse.ArgumentParser()
parse.add_argument("-p", "--password", help="Pon aqui el hash de la password.", required=False)
parse.add_argument("-w", "--wordlist", help="Añade aqui el archivo del wordlist", required=True)
parse.add_argument("-a", "--archivo", help="Añade el fichero de hashes", required=False) #TODO Implementar la posibilidad de usuario:password
parse.add_argument("-f", help="Añade el nombre del hash del cifrado(Admitidos: md5, sha1, sha256, sha512, blake2)", required=True)
args = parse.parse_args()

def check_hash():
    if args.archivo != None:
        array_hash = open(args.archivo, "r")
        for hash in array_hash:
            checker(hash, args.wordlist)
        array_hash.close()
    else:
        hash = args.password
        checker(hash, args.wordlist)

def checker(hash, wordlist):
    word = open(wordlist, "r")
    hash_to_check = hash.strip()
    for linea in word:
        contraseña = linea.strip()
        if args.f == "sha1":
            hash_dict = hashlib.sha1(contraseña.encode()).hexdigest()
        elif args.f == "md5":
            hash_dict = hashlib.md5(contraseña.encode()).hexdigest()
        elif args.f == "sha256":
            hash_dict = hashlib.sha256(contraseña.encode()).hexdigest()
        elif args.f == "sha512":
            hash_dict = hashlib.sha512(contraseña.encode()).hexdigest()
        elif args.f == "blake2":
            hash_dict = hashlib.blake2b(contraseña.encode()).hexdigest()

        if hash_to_check == hash_dict:
            return print(f'El hash: {hash.strip()} es la palabra: {linea}')
            break
    print(f"No esta en el wordlist, prueba con otro. -- {hash.strip()}\n")
    word.close()


check_hash()