import numpy as np


pi = np.array([0.6,0.4])

A = np.array([[0.7,0.3],[0.4,0.6]])

B = np.array([[0.5,0.5],[0.2,0.8]])

sequences = ['000','001','010','011','100','101','110','111']

s=0
for i in sequences:
    
    a = int(i[0])
    b = int(i[1])
    c = int(i[2])

    prob = pi[a]*B[a,1]*A[a,b]*B[b,1]*A[b,c]*B[c,1]
    s+=prob
    print (prob)

print (s)