import random
import os
from netTools import port_scan, getHost

def genIp():
    ip = ".".join(map(str, (random.randint(0, 255)for _ in range(4))))
    return ip


def writeFile(content):
    with open('ip', 'a') as f:
        f.write(content + "\n")



def ping(hostname):
    #example
    response = os.system("ping -n 1 -w 2 " + hostname + " > NULL")

    #and then check the response...
    if response == 0:
        print (hostname + ' is up!')
        writeFile(hostname + ":"  + " ports: " +port_scan(hostname))
        # + str(getHost(hostname))
    else:
        print (hostname + ' is down!')
    





for i in range(1,100):
    ping(genIp())