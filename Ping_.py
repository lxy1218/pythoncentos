import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *
def Ping(ip):
    ping_pkt = IP(dst=ip)/ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        return 1
    else:
        return 0
if __name__ == "__main__":
    for ip in ["192.168.0.128","192.168.0.129"]:
        #print(ip)
        result = Ping(ip)
        if result ==1:
            print(ip ,"通了")
        if result != 1:
            print(ip ,"没通")