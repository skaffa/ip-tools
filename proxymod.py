import requests
import json
import random
global proxytype
global server


def http():
    array = httpr.split('\n')
    server = random.choice(array)
    server = {"http":server}




httpr = requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=elite&simplified=true').text
socks4r = requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all').text 
socks5r = requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all').text





#MAKE PART OF WHATSMYIP MODULE
def own():
    global server
    server = requests.get('https://ifconfig.me/ip').text
    print(server)
###############################

def socks4():
    array = socks4r.split('\n')
    server = random.choice(array)

def socks5():
    array = socks5.split('\n')
    server = random.choice(array)

def custom():
    server = (input('Enter proxy IP including port:\n>'))






#TODO#
#
#Add optional country selection
#Add anonimity selector for http proxy
#Add function to specify own proxy list to choose random proxy from