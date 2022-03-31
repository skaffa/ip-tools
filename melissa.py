import requests
import json
import time
import random

print('Starting melissa...')

def request(self):

    httpr = requests.get('http://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all').text
    array = httpr.split('\n')
    server = random.choice(array)
    server = {"http":server}
    
    print('\nMaking request from proxy ' + str(server))

    #headers["X-Real-IP"] = ""
    #headers = {'Accept': '*/*', 'X-User-IP': '6.3.8.4'}
    try:
        print('Fetching results...')
        url = 'https://www.melissa.com/v2/lookups/iplocation/ip/?ip=%s&site=&fmt=json&id='%self
        x = requests.get(url, proxies=server, verify=True)
        array = x.text.split(',')
        print('\nShowing results for ' + self)
        print("\n ==========================\n")
        for i in array:
            i = i.replace('\"', "")
            i = i.replace(' :', ":")
            i = i.replace(':', ": ")
            i = i.replace('{', "")
            i = i.replace('}', "")
            i = i.replace('[', "")
            i = i.replace(']', "")
            print(" "+i+"\n")
        print("\n ==========================\n")
    except:
        print('Error, couldn\'t fetch data')

destiny = input("\nEnter IP to check, leave empty to use own IP:\n>")
if destiny == '':
    destiny = requests.get('https://ifconfig.me/ip').text
    print('No IP specified, using own IP')


request(destiny)



# MADE BY SKAFFA
# https://github.com/skaffa