# python-ciber

Scripts de Python para ciber

![Badge en Desarollo](https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green)
![Stars](https://img.shields.io/github/stars/brunolopezbarcia/python-ciber?style=social)

## Scripts Network.

### IP_Scanner

Este script permite escanear los hosts que estan activos en una red. Se permite la salida tanto por consola como que
salga las Ips en un archivo.

##### TODO

* [ ]  Permitir que salga solo las Ips o con mas info en base a las opciones que se pasen.

#### Ejecutar script

```bash
python3 src/NetworkHacking/ip_scanner.py -n 192.168.0.0/24 [-o salida.txt] 
```

Para obtener informacion relativa al comando podemos lanzar lo siguiente:

```bash
python3 src/NetworkHacking/ip_scanner.py -h
```

## Scripts Web

### Fuzzing Scanner

Este script permite realizar fuzzing, con el diccionario que provee la herramienta o uno personalizado sobre cualquier, url o IP.

#### TODO

* [ ]  Salida por archivo de texto
* [ ]  Salida con solo url o con informacion sobre todas las urls escanedas.

#### Ejecutar Scripts

```bash
python3 src/WebHacking/fuzzing_scanner.py --url URL_A_ESCANEAR [-w wordlist]
```

Para obtener informacion relativa al comando podemos lanzar lo siguiente:

```bash
python3 src/WebHacking/fuzzing_scanner.py -h
```

Autor: Bruno López Barcia
