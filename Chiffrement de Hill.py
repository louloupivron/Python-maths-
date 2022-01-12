from math import *
Alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
x=input("chiffrage ou déchiffrage ?")
l=int(input("combien de lettres ?"))

if x=="chiffrage":
 for I in range(l):
  a=input()
  b=input()
  x1=Alphabet.index(a) 
  x2=Alphabet.index(b)
  X=[ [x1],[x2] ]
  #print ("X :", X)
  
  Q = [ [6, 3], [5, 3] ]
   
  n=len(Q) # nombre de lignes de Q
  m=len(X[0]) # nombre de colonnes de X
  p=len(X) # nombre de lignes de X
   
  C = [[0]*m for i in range(n)] # matrice de n lignes et m colonnes
   
  # parcourir les lignes de Q
  for i in range(n):
      # parcourir les colonnes de X
      for j in range(m):
          # parcourir les lignes de X
          for k in range(p):
              C[i][j] += Q[i][k] * X[k][j]
   
  #print("Q : ", Q)
  #print("X : ", X)
  #print("Q * X : ", C)
  r1=C[0][0]%26
  r2= C[1][0]%26
  print Alphabet[r1], Alphabet[r2]
  
if x=="déchiffrage":
  for I in range(l):
   a=input()
   b=input()
   r1=Alphabet.index(a) 
   r2=Alphabet.index(b)
   x1=(r1-r2)%26
   x2=(7*r1+2*r2)%26
   print Alphabet[x1], Alphabet[x2]
  
  
  
  
