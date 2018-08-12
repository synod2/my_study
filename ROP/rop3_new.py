#-*- coing : utf-8 -*-
from pwn import *

p = process(["./rop3_new"])
p.interactive()
pause()
