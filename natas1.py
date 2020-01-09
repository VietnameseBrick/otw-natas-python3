import requests
import re

u='natas1'
p='gtVrDuiDfck831PqWsLEZy5gyDz1clto'
l=f'http://{u}.natas.labs.overthewire.org'
s = requests.Session()
s.auth = (u, p)
resp=s.get(l)
t=resp.text

print(re.findall('<!--The password for natas2 is (.*) -->',t)[0])
