import numpy as np

m1 = np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])

m2 = np.array([[9,8,7],
               [6,5,4],
               [3,2,1]])

s = 2

print("addition is ",m1+m2)
print("subtraction is ",m1-m2)
print("scalar multiplication is ",m1*s)
print("scalar division is", m1/s)
print("matrix and scalar addition ", m1+s)
print("size of matrix:",len(m1),"X",len(m1[0]))
print("value of m1 23 is", m1[2-1][3-1])