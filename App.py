from util.properties import getHosts
from util.scanner import scan_ports

def main():
    for host in getHosts():
        print("\nScanning ports on " + host + " ...")
        ports = list(scan_ports(host))
        print("\nDone.")

        print(str(len(ports)) + " ports available.")
        print(ports)

if __name__ == "__main__":
    main()