#PyPing2 main module

import requests
import time
import sys
def ping(ip):
    """ Pings an ip with a HTTP GET request and returns the ping time in seconds.

    Args:
        ip (str):  domain name or an ip address.

    Returns:
        _type_: ping_time (float) , HTTP code (int)
    """
    if "https://" in ip:
        pass
    else:
        ip = "https://"+ip
    time_start = time.time()
    request = requests.get(ip)
    time_end = time.time()
    pingtime = time_end - time_start
    code = request.status_code
    return pingtime,code
def multiping(ips):
    """ Pings multiple ips with a HTTP GET request and returns the ping time in seconds.

    Args:
        ips (list):  domain name or an ip address.
    
    Returns:
        _type_: ping_times (list) , HTTP codes (list)
    """
    pingtimes = []
    codes = []
    for i in ips:
        if "https://" in i:
            pass
        else:
            i = "https://"+i
        time_start = time.time()
        request = requests.get(i)
        time_end = time.time()
        pingtime = time_end - time_start
        code = request.status_code
        pingtimes.append(pingtime)
        codes.append(code)
    return pingtimes,codes
def demo():
    print("Demo of PyPing2")
    print("Ping time of google.com:"+str(ping("www.google.com")[0]))
    print("Multiping of google.com and github.com:"+str(multiping(["www.google.com","www.github.com"])[0]))