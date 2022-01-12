
x=input("chiffrage ou déchiffrage ?")
r=int(input("combien de lettres ?"))
a=0
if x=="chiffrage":
 for i in range(r):
  a=input() 
  b=Alphabet.index(a)
  c=(3*b+7)%26 
  print(Alphabet[c])
elif x=="déchiffrage":
 for i in range(r):
  a=input() 
  b=Alphabet.index(a)
  c=(9*b+15)%26 
  print(Alphabet[c])
 
 


