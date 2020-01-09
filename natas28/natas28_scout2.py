import requests, base64
import binascii
import string

url="http://natas28.natas.labs.overthewire.org/index.php"
s=requests.Session()
s.auth=('natas28','JWwR438wkgTsNKBbcJoowyysdM82YjeF')

charset = string.ascii_lowercase
sample='x'*8
out=''

for c in charset:
    data={'query':sample+c}
    r=s.post(url,data=data)
    cipher = r.url.split('=')[1]
    cipher = requests.utils.unquote(cipher)
    line=f'sample len: {len(sample)}\t|{cipher}\n'
    out+=line

with open('scout2.txt','w') as f:
    f.write(out)
