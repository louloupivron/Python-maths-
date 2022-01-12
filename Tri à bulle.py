li=[5,56,45,2,90,4,345,36,65,754,34,6]
count=1
while count==1:
 count=0 
 for n in range(0,len(li)-1):
  if li[n]>li[n+1]:
    c=li[n]
    li[n]=li[n+1]
    li[n+1]=c
    count=1
print li  