from pwn import  *

p = remote("crypto.task.ctf.codeblue.jp", 13337)

print p.recvline()
print p.recvline()

payload = "aaaaaaaaaaaaaaaalazy1"

p.sendline(payload)
sleep(0.5)

print p.recvuntil("ciphertext:")

p.recvline()
cipher = p.recvline() #recieve cipher text 
#print "\nCipher : ",cipher

print p.recvuntil("hex.")
print p.recvline()

p.sendline("exit")
sleep(0.5)

print p.recvline()

payload2 = "aaaaaaaaaaaaaaaalazy1"
p.sendline(payload2)
print p.recvline()