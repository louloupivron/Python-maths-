from random import *
li=[randint(1,2000000),randint(1,2000000),randint(1,2000000),randint(1,2000000),randint(1,2000000)]
Min=10**100
Max=0
for i in li :
  if i<Min:
    Min=i; 
print("min:",Min)
for i in li :
  if i>Max:
    Max=i; 
print("max:",Max)
print("étendue:",Max-Min)



print(max(li))