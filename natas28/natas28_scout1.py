import requests, base64
import binascii

url = "http://natas28.natas.labs.overthewire.org/index.php"
s = requests.Session()
s.auth = ('natas28', 'JWwR438wkgTsNKBbcJoowyysdM82YjeF')

sample = 'x'
out = ''

while len(sample) < 16:
    data = {'query': sample}
    r = s.post(url, data=data)
    cipher = r.url.split('=')[1]
    cipher = requests.utils.unquote(cipher)
    line = f'sample len: {len(sample)}\t|{cipher}\n'
    out += line
    sample += 'x'

with open('scout1.txt', 'w') as f:
    f.write(out)
