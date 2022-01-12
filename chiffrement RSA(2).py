from random import *
from math import *
print("choix de la clé publique"); 
print("plus vos entiers sont grands plus la sécurité du système est grande");
print("ceux la sont grands par exemple: (199,599,1597,4211,6569,9103,)");
p=int(input("un nombre premier ?"));q=int(input("un autre ?"));
N=p*q ; print ("N:", N)
f=n=(p-1)*(q-1); print ("n:", n)
a=0


while a!=1:
 c=a=int(input ("CHOISSISEZ UN NOMBRE PREMIER AVEC n" ))
 r=1
 while r!=0:                                                          #pgcd(n,a)
  r=n%a 
  if r!=0:
   n=a 
   a=r
 
 
 if a!=1:                                 #INDIQUE SI LE NOMBRE CHOISI EST PREMIER AVEC n
  print "CELUI LA N'EST PAS BON "


print "VOICI VOTRE CLÉ PUBLIQUE", (N,c)                               #CLÉ PUBLIQUE


X=input( "chiffrage ou déchiffrage ?") 


if X=="chiffrage":                                                    #CHIFFRAGE
  e=int(input("CHOISSISEZ LE NOMBRE QUE VOUS SOUHAITEZ CHIFFRER")) 
  print "LE NOMBRE CHIFFRÉ EST:", e**c%N


elif X=="déchiffrage":                                                #DÉCHIFFRAGE
 u=0
 d=0
 while u!=1:                 
  u=(c*d%f)
  d=d+1
  

 print "VOICI VOTRE CLÉ PRIVÉE", d-1                                   #CLÉ PRIVÉE


 x=int(input("CHOISSISEZ LE NOMBRE QUE VOUS SOUHAITEZ DÉCHIFFRER?"))    
 print "LE NOMBRE DÉCHIFFRÉ EST", x**(d-1)%N



  
  
  
  

    
