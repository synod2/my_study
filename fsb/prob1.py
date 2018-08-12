from pwn  import *
import os
import sys

p = process("./problem1")

print p.recv()
'''
payload = "1"
p.sendline(payload)

print p.recv()

payload2 = "a"*30
p.sendline(payload2)

print p.recv()


payload3 = "a"*30
p.sendline(payload3)

print p.recv()
'''
p.interactive()
