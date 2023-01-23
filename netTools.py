import socket
import sys
from socket import AF_INET
from socket import SOCK_STREAM, gethostbyaddr
from socket import socket

from concurrent.futures import ThreadPoolExecutor




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
                print(f'> {host}:{port} open')
                opened += str(port) + " "
    return opened

def test_port_number(host, port):
    # create and configure the socket
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.settimeout(2)
        try:
            # attempt to connect
            sock.connect((host, port))
            return True
        except:
            return False
 

