import random
import os
from netTools import port_scan, getHost, ping

def genIp():
    ip = ".".join(map(str, (random.randint(0, 255)for _ in range(4))))
    return ip







for i in range(1,100):
    ping(genIp())