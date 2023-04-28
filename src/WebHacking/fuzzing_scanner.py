import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="URL a Procesar", required=True)
parser.add_argument("-w", "--wordlist", help="Diccionario a usar", required=False, default="combined_directories.txt")
args = parser.parse_args()


def check_url(URL_INICIAL, wordlist):
    URL_inicial = URL_INICIAL
    i = 1
    f = open(wordlist, "r")
    for linea in f:
        URL_ANALIZAR = URL_inicial + linea
        response = requests.get(f"{URL_ANALIZAR}")
        status_code = response.status_code
        if status_code == 200:
            print(f"Peticion: {i} -- Existe -- {URL_ANALIZAR}")
            i = i + 1
        else:
            print(f"Peticion: {i} -- No Existe -- {URL_ANALIZAR}")
            i = i + 1
    f.close()


check_url(args.url, args.wordlist)
