import requests
import re

u='natas0'
p='natas0'
l=f'http://{u}.natas.labs.overthewire.org'
s = requests.Session()
s.auth = (u, p)
resp=s.get(l)
t=resp.text

print(re.findall('<!--The password for natas1 is (.*) -->',t)[0])

