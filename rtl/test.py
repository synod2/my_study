from pwn import *

f = open("./flag.txt","r")
print f.readline()

f.close()