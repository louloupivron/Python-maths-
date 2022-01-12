from random import *
from math import *
print("choose your public key"); 
print("for more safety choose big numbers");
print("those are big ones (199,599,1597,4211,6569,9103,)");
p=int(input("prime number"));q=int(input("another one"));
N=p*q ; print ("N:", N)
f=n=(p-1)*(q-1); print ("n:", n)
a=0
while a!=1:
 c=a=int(input ("CHOOSE NUMBER COPRIME WITH n" ))
 r=1
 while r!=0:      #pgcd(n,a)
  r=n%a 
  if r!=0:
   n=a 
   a=r
 if a!=1:
  print "THIS ONE IS NOT CORRECT "
print "your public key must be", (N,c)

X=input( "chiffrage ou déchiffrage ?") 
if X=="chiffrage":
  e=int(input("choose now the number you want to encrypt")) 
  print " the encrypted number is", e**c%N
elif X=="déchiffrage":
 u=0
 d=0
 while u!=1:                 
  u=(c*d%f)
  d=d+1
 x=int(input("what number do you want to decrypt?"))
 print x**(d-1)%N



  
  
  
  

    
