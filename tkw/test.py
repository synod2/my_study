#-*- coding: utf-8 -*-
import os
import copy

P = "aaaaaaaaaaaaaaaalazy0"

sbox = [12, 5, 6, 11, 9, 0, 10, 13, 3, 14, 15, 8, 4, 7, 1, 2]
K = [144, 157, 178, 58, 83, 165, 8, 83, 220, 58, 125, 204, 21, 36, 186, 89]
WORDFILTER = 0xF

MixColMatrix = [
	[4,  1, 2, 2],
	[8,  6, 5, 6],
	[11,14,10, 9],
	[2,  2,15,11],
]


def FieldMult(a,b):
  ReductionPoly = 0x3
  x = a
  ret = 0
  for i in range(0,4):
    if (b>>i)&1 == 1: 
        ret ^= x
    if (x&0x8) != 0:
      x <<= 1
      x ^= ReductionPoly
    else: x <<= 1
  return ret&WORDFILTER



origin = [0]*16
print P[-5:-1]
ksbits = len(K)*8
keyNibbles = [0]*32
keyres1 = [0]*32
userkey = K
state = [[0 for i in range(4)] for j in range(4)]
state2 = [[0 for i in range(4)] for j in range(4)]
def AddConstants(r):
  global state
  RC = [
		0x01, 0x03, 0x07, 0x0F, 0x1F, 0x3E, 0x3D, 0x3B, 0x37, 0x2F,
		0x1E, 0x3C, 0x39, 0x33, 0x27, 0x0E, 0x1D, 0x3A, 0x35, 0x2B,
		0x16, 0x2C, 0x18, 0x30, 0x21, 0x02, 0x05, 0x0B, 0x17, 0x2E,
		0x1C, 0x38, 0x31, 0x23, 0x06, 0x0D, 0x1B, 0x36, 0x2D, 0x1A,
		0x34, 0x29, 0x12, 0x24, 0x08, 0x11, 0x22, 0x04
	]
  print "before state:",state
  state[1][0] ^= 1
  state[2][0] ^= 2
  state[3][0] ^= 3

  state[0][0] ^= (LED>>4)&0xf
  state[1][0] ^= (LED>>4)&0xf
  state[2][0] ^= LED & 0xf
  state[3][0] ^= LED & 0xf

  tmp = (RC[r] >> 3) & 7
  state[0][1] ^= tmp
  state[2][1] ^= tmp
  tmp =  RC[r] & 7
  state[1][1] ^= tmp
  state[3][1] ^= tmp
  
  # rewind
  '''
  tmp =  RC[r] & 7
  state[1][1] ^= tmp
  state[3][1] ^= tmp
  
  tmp = (RC[r] >> 3) & 7
  state[0][1] ^= tmp
  state[2][1] ^= tmp
  
  state[0][0] ^= (LED>>4)&0xf
  state[1][0] ^= (LED>>4)&0xf
  state[2][0] ^= LED & 0xf
  state[3][0] ^= LED & 0xf
  
  state[1][0] ^= 1
  state[2][0] ^= 2
  state[3][0] ^= 3
  print "after state:",state
  '''



P = P[0:16].decode("hex")

p_data = []

for i in range( len(P) ):
    p_data.append( ord(P[i]) )


for i in range(0,16):
    if (i%2) == 1: 
        state[i/4][i%4] = p_data[i>>1]&0xF
        #print i," state:",state
    else: 
        state[i/4][i%4] = (p_data[i>>1]>>4)&0xF
        # print i," state:",state
p_data = copy.deepcopy(state)
#print "\ndata input: ",p_data,"\n" #알파벳 값을 그대로 16진수값으로 변환  


for i in range(0,ksbits/4):
    if (i%2) == 1: 
        keyNibbles[i] = userkey[i>>1]&0xF
        #print "\n",i,"userkey : ",userkey[i>>1],"nib : ",keyNibbles[i]
    else: 
        keyNibbles[i] = (userkey[i>>1]>>4)&0xF
        #print "\n",i,"userkey2 : ",userkey[i>>1]>>4,"nib : ",keyNibbles[i]
        
print "\n result random : ",keyNibbles,"\n"

for i in range(0,ksbits/4):
    if (i%2) == 0:
        #print i/2
        origin[i/2] = int(str(hex(keyNibbles[i])[2:])+str(hex(keyNibbles[i+1])[2:]),16)

#print origin
LED = ksbits
RN = 48
print "LED:",LED

print "\nbefore state:",state
'''
#print "\ndata input: ",p_data,"\n"
for i in range(0,4): #첫번쨰 연산 , 랜덤키 앞쪽 절반 연산.
    for j in range(0,4):
        state[i][j] ^= keyNibbles[(4*i+j+1*16)%(LED/4)] #p_data ^ keybib = state
 
print "\nafter state:",state

for i in range(0,4): #첫번쨰 연산 복호화 연산 
    for j in range(0,4):
        #print (4*i+j+0*16)%(LED/4)
       # print "\n",state[i][j] ^ p_data[i][j]
        keyres1[(4*i+j+1*16)%(LED/4)] = state[i][j] ^ p_data[i][j] 
print "\nafter state:",keyres1
'''
output = [0]*8
ret = ""

for i in range(0,8):
    output[i] = ((state[(2*i)/4][(2*i)%4] & 0xF) << 4) | (state[(2*i+1)/4][(2*i+1)%4] & 0xF)
    print output[i]
    ret += chr( output[i])
ret =ret.encode('hex')
print "result : ",ret

P = ret[0:16].decode("hex")

p_data = []

for i in range( len(P) ):
    p_data.append( ord(P[i]) )


for i in range(0,16):
    if (i%2) == 1: 
        state[i/4][i%4] = p_data[i>>1]&0xF
        #print i," state:",state
    else: 
        state[i/4][i%4] = (p_data[i>>1]>>4)&0xF
        # print i," state:",state
p_data = copy.deepcopy(state)

print p_data

'''
for i in range(0,4): #첫번쨰 연산 , 랜덤키 앞쪽 절반 연산.
    for j in range(0,4):
        state[i][j] ^= keyNibbles[(4*i+j+0*16)%(LED/4)] #p_data ^ keybib = state
 
print "\nafter state:",state
#print "\ndata input: ",p_data,"\n"


for i in range(0,4): #첫번쨰 연산 복호화 연산 
    for j in range(0,4):
        #print (4*i+j+0*16)%(LED/4)
       # print "\n",state[i][j] ^ p_data[i][j]
        keyres1[(4*i+j+0*16)%(LED/4)] = state[i][j] ^ p_data[i][j] 
'''
#print "\nkey res1:",keyres1
'''
AddConstants(4)

for i in range(0,4): #세번째 연산 
    for j in range(0,4):
        state[i][j] = sbox[state[i][j]] 

print "\nafter state:",state

for i in range(0,4): #세번째 연산 복호화 subcell
    for j in range(0,4):
       # print state[i][j]
        state2[i][j] = sbox.index(state[i][j])

#print "\nafter state2:",state2


tmp = [0]*4 #네번쨰 연산
for i in range(1,4):
    for j in range(0,4):
        tmp[j] = state[i][j]
    for j in range(0,4):
        state[i][j] = tmp[(j+i)%4]
        
print "\nafter state1:",state        
'''
'''
tmp = [0]*4 #네번쨰 연산
for i in range(1,4):
    for j in range(0,4):
        tmp[j] = state[i][j]
    for j in range(0,4):
        state[i][j] = tmp[(j+i)%4]
        
tmp = [0]*4 #네번쨰 연산
for i in range(1,4):
    for j in range(0,4):
        tmp[j] = state[i][j]
    for j in range(0,4):
        state[i][j] = tmp[(j+i)%4]

tmp = [0]*4 #네번쨰 연산
for i in range(1,4):
    for j in range(0,4):
        tmp[j] = state[i][j]
    for j in range(0,4):
        state[i][j] = tmp[(j+i)%4]    
        
#print "\nafter state:",state 


tmp = [0]*4
for j in range(0,4):
    for i in range(0,4):
        sum = 0
        for k in range(0,4):
            sum ^= FieldMult(MixColMatrix[i][k], state[k][j]) # state[i][j] = sum ^ FieldMult(MixColMatrix[i][k], state[k][j])
            tmp[i] = sum
            
            sum = fm(0,0) ^ 0
            tmp[0] = fm(0) ^ 0
            tmp[1] = fm(1) ^ fm(0) ^ 0 
            tmp[2] = fm(2) ^ fm(1) ^ fm(0) ^ 0 
            tmp[3] = fm(3) ^ fm(2) ^ fm(1) ^ fm(0) ^ 0 
            
            
    for i in range(0,4):
        state[i][j] = tmp[i]





print "\nafter state:",state
'''


'''
lazy = int(P[-1])
print "Nice.", lazy

P = P[0:16].decode("hex")

k_data = []
p_data = []
for i in range( len(K) ):
  k_data.append( ord(K[i]) )
for i in range( len(P) ):
  p_data.append( ord(P[i]) )

print "plaintext: "
print p_data

if lazy == 0:
      print "lazy in 0"
else: 
      print "fail"
      '''