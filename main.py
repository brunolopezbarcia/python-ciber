from flask import Flask, jsonify, request
import requests
from src.NetworkHacking.ip_scanner import NetWorkScan_module

from src.WebHacking.fuzzing_scanner import check_url

app = Flask(__name__)



@app.route('/urlscanner', methods=['GET'] )
def url_scnaner_API():
    url = request.args.get('url')
    wordlist = './prueba_url.txt'
    API = True
    return check_url(url, wordlist, API)

@app.route('/ipscanner', methods=['GET'])
def ip_scanner_API():
    ip = request.args.get('ip')
    API = True
    return NetWorkScan_module(ip, API)

if __name__ == '__main__':
    app.run(debug=True)





