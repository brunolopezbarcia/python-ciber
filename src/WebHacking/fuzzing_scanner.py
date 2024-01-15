import requests
import argparse
from flask import jsonify
import logging

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="URL a Procesar", required=False)
parser.add_argument("-w", "--wordlist", help="Diccionario a usar", required=False, default="combined_directories.txt")
args = parser.parse_args()



logs_url = logging
logs_url.basicConfig(filename='logs/url_scrapper.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def check_url(URL_INICIAL, wordlist, API):
    URL_inicial = URL_INICIAL
    i = 1
    f = open(wordlist, "r")
    
    if API == True:
        if URL_INICIAL is not None:
            urls = []
            with open(wordlist, "r") as f:
                for linea in f:
                    linea = linea.strip()  # Remove leading/trailing whitespace
                    URL_ANALIZAR = URL_inicial + linea
                    response = requests.get(URL_ANALIZAR)
                    status_code = response.status_code

                    url = {
                        "Url": URL_ANALIZAR,
                        "Existe": "Si" if status_code == 200 else "No",
                        "Status Code": status_code
                    }
                    logs_url.info(url)
                    urls.append(url)
                    i += 1
            email_sender(urls)
            return jsonify({"urls": urls})
        else:
            warning_message = {
                "Url": None,
                "Message": "Se debe de pasar una url a escanear."
            }
            logs_url.warning(warning_message)
            return jsonify(warning_message)
        
    else:
        for linea in f:
            URL_ANALIZAR = URL_inicial + linea
            response = requests.get(URL_ANALIZAR)
            status_code = response.status_code
            if status_code == 200:
                message = (f"Peticion: {i} -- Existe -- {URL_ANALIZAR} -- API = {API}")
                print(message)
                logging.info(message)
                i = i + 1
            else:
                message = (f"Peticion: {i} -- No Existe -- {URL_ANALIZAR} -- API = {API}")
                print(message)
                logging.info(message)
                i = i + 1
        f.close()
        


if args.url:
    check_url(args.url, args.wordlist, API=False)   

