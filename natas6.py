from bs4 import BeautifulSoup as bs
import requests
import re

u='natas6'
p='aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'
#l=f'http://{u}.natas.labs.overthewire.org/includes/secret.inc'
l=f'http://{u}.natas.labs.overthewire.org/'
resp=requests.post(l,data={"secret":"FOEIUWGHFEEUHOFUOIU","submit":"submit"},auth=(u, p))
t=resp.text
print(re.findall(r'Access granted. The password for natas7 is (.*)',t)[0])
