import argparse
import networkscan

parse = argparse.ArgumentParser()
parse.add_argument("-n", "--network", help="Network IP", required=True)
parse.add_argument("-o", "--output", help="Output file", required=False)
parse.add_argument("-v", "--verbose", help="Verbose(Aun por implementar)", required=False, type=bool)

args = parse.parse_args()


def NetWorkScan_module(network):
    scan = networkscan.Networkscan(network)
    scan.run()

    print("La red " + network + " ha sido escaneada")
    if (args.output) == None:
        for i in scan.list_of_hosts_found:
            print("La IP: " + i + " esta disponible")
    else:
        for i in scan.list_of_hosts_found:
            with open(args.output, "a") as f:
                f.write("La IP: " + i + " esta disponible" + "\n")
                f.close()


NetWorkScan_module(args.network)
