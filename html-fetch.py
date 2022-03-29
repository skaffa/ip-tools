import requests
import os

print('Starting html-fetch...')

url = input('Enter URL to webpage\n>')
httpr = requests.get(url).text

if not os.path.isdir('saved-webpages'):
    os.makedirs('saved-webpages')






#import time?
#import datetime?
#save with datetime format time + website url in filename, slashes removed and replaced by placeholder character
