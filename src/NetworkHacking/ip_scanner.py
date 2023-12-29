import argparse
from flask import jsonify
import networkscan
import logging

parse = argparse.ArgumentParser()
parse.add_argument("-n", "--network", help="Network IP", required=False)
parse.add_argument("-o", "--output", help="Output file", required=False)
parse.add_argument("-v", "--verbose", help="Verbose(Aun por implementar)", required=False, type=bool)

args = parse.parse_args()

logging.basicConfig(filename='logs/ip_checker.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def NetWorkScan_module(network,API):
    if API == True:
        scan = networkscan.Networkscan(network)
        scan.run()
        ips = [network]
        for i in scan.list_of_hosts_found:
            
            ip = {
                "IP:": i,
                "Existe": "SI"
            }
            ips.append(ip)
            logging.info(ip)
        return jsonify(ips)
    else:        
        scan = networkscan.Networkscan(network)
        scan.run()

        red = "La red " + network + " ha sido escaneada"
        print(red)
        print(scan.list_of_hosts_found)
        if (args.output) == None:
            for i in scan.list_of_hosts_found:
                message = "La IP: " + i + " esta disponible"
                logging.info(red + message)
                print(message)
        else:
            for i in scan.list_of_hosts_found:
                with open(args.output, "a") as f:
                    message = "La IP: " + i + " esta disponible"  
                    f.write(message + "\n")
                    logging.info(red + message)
                    f.close()

if args.network:
    NetWorkScan_module(args.network, API=False) 