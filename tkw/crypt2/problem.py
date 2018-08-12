from Crypto.Util.number import *
#from key import FLAG

size = 128
rand_state = getRandomInteger(size//2)

def keygen(size):
  q = getPrime(size)
  k = 2
  while True:
    p = q * k + 1
    if isPrime(p):
      break
    k += 1
  g = 2
  while True:
    if pow(g, q, p) == 1:
      break
    g += 1
  A = getRandomInteger(size) % q
  B = getRandomInteger(size) % q
  x = getRandomInteger(size) % q
  h = pow(g, x, p)
  return (g, h, A, B, p, q), (x, )

def rand(A, B, M):
  global rand_state
  #print "\nrand_state1 : ",rand_state
  k = (A * rand_state + B) % M
  print "\nmult:",(A * k + B) % M
  rand_state, ret = (A * rand_state + B) % M, rand_state
  #print "\nrand_state2 : ",rand_state
  print "\nret : ",rand_state
  return ret

def encrypt(pubkey, m): #m : message
  g, h, A, B, p, q = pubkey
  assert 0 < m <= p
  r = rand(A, B, q)
  print "r is:",r
  c1 = pow(g, r, p)
  c2 = (m * pow(h, r, p)) % p
  return (c1, c2)

def decrypt(c1,c2,privkey,pubkey) :
  g, h, A, B, p, q = pubkey
  x, = privkey
  ax = pow(c1,x,p)
  print "\ninverse",inverse(ax,p)
  plain = (c2*inverse(ax,p))%p
  return plain
  
  
pubkey, privkey = keygen(size)

print pubkey,"\nprv:",privkey
#m = bytes_to_long(FLAG)
m = bytes_to_long("hello")

c1, c2 = encrypt(pubkey, m)
c1_, c2_ = encrypt(pubkey, m)

#print pubkey
print (c1, c2)
print (c1_, c2_)

print decrypt(c1,c2,privkey,pubkey)
print decrypt(c1_,c2_,privkey,pubkey)
#print privkey
#print "plain : ",m