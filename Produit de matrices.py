A = [ [3, 1, 5], [9, 8, -1], [10, 12, 2] ]
B = [ [8, -1, 8], [2, 1, 3], [18, 2, 32] ]
 
n=len(A) # nombre de lignes de A
m=len(B[0]) # nombre de colonnes de B
p=len(B) # nombre de lignes de B 
 
C = [[0]*m for i in range(n)] # matrice de n lignes et m colonnes
 
# parcourir les lignes de A
for i in range(n):
    # parcourir les colonnes de B
    for j in range(m):
        # parcourir les lignes de B
        for k in range(p):
            C[i][j] += A[i][k] * B[k][j]
 
print("A : ", A)
print("B : ", B)
print("A * B : ", C)
