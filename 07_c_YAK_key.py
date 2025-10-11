#YAK authenticated key exchange protocol


import random 
import Crypto.Util.number

g=2
a=random.randint(0,2e16)
b=random.randint(0,2e16)

x=random.randint(0,2e16)
y=random.randint(0,2e16)

bits=128
p=Crypto.Util.number.getPrime(bits,randfunc=Crypto.Random.get_random_bytes)

Apub=pow(g,a,p)
Bpub=pow(g,b,p)

A=pow(g,x,p)
B=pow(g,y,p)

KA=pow(B*Bpub,x+a,p)

KB=pow(A*Apub,y+b,p)

print ("Prime: ",p)
print ("g ",g)

print ("\nAlice public key: ",Apub)
print ("Bob public key: ",Bpub)

print ("\nAlice secret:\t",a)
print ("Bob secret:\t",b)

print ("\nAlice passes:\t",A)
print ("Bob passes:\t",B)

print ("\nAlice key:\t",KA)
print ("Bob key:\t",KB)
