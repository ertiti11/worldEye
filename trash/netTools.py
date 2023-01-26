import socket
import sys
from socket import AF_INET
from socket import SOCK_STREAM, gethostbyaddr
from socket import socket
import os
from concurrent.futures import ThreadPoolExecutor
from getServices import scan
from multiport import scan_ports


def writeFile(content):
    with open('ip', 'a') as f:
        f.write(content + "\n")



def ping(hostname):
    #example
    response = os.system("ping -n 1 -w 2 " + hostname + " > NULL")

    #and then check the response...
    if response == 0:
        
        writeFile(hostname + ":"  + " ports: " + str(scan_ports(hostname,1)))
        print(hostname + ":"  + " ports: " + str(scan_ports(hostname,1)))
        # print(str(getHost(hostname)))
    else:
        pass
    

def getHost(ip):
    try:
        host = gethostbyaddr(ip)
        print('Address: ', ip, '\n' 'Host: ', host)
    except:
        pass



# scan port numbers on a host
def port_scan(host):
    opened = ""
    ports = range(10000)
    print(f'Scanning {host}...')
    with ThreadPoolExecutor(len(ports)) as executor:
        results = executor.map(test_port_number, [host]*len(ports), ports)
        for port,is_open in zip(ports,results):
            if is_open:
                scan(host,port,1)
                # print(f'> {host}:{port} open')
                opened += str(port) + " "
    return opened

def test_port_number(host, port):
    # create and configure the socket
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.settimeout(2)
        try:
            # attempt to connect
            if sock.connect((host, port)):
                try:
                    service = socket.getservbyport(port)
                    print(str(port) + "/TCP" + "  " + service)
                except socket.error:
                    print(str(port) + "/TCP" + "  " + "Unknown")
                except KeyboardInterrupt:
                    print("[-] Exiting!")
                    exit(1)
            return True
        except:
            return False
 

