from bs4 import BeautifulSoup as bs
import urllib
import base64
import binascii
import requests
import re

u='natas11'
p='U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'
l=f'http://{u}.natas.labs.overthewire.org'
resp=requests.post(l,auth=(u, p))
d=resp.cookies["data"]
print(binascii.hexlify(base64.b64decode(urllib.parse.unquote(d))))
