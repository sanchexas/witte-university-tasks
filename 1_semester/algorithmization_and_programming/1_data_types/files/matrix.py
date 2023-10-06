matrix = open("matrix.txt")
mat = matrix.read().split()
 
w = len(mat)
i = 1
while i < w + 1:
    if w/i == i:
        break
    i = i + 1
 
mat = mat[::i+1]
mat_n = [int(j) for j in mat]
 
print(sum(mat_n))