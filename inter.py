from math import*
import numpy as np
def interpolação(x,y,X):
    n=len(x)
    a=np.zeros((n,n),float)
    i=0
    j=0
    k=n-1
    
    while i<n:
        while j<n:
           a[i][j]=(x[i])**(k)
           k=k-1
           j=j+1
        j=0
        i=i+1
        k=n-1
    inv=np.linalg.inv(a)
    c=np.dot(inv,y)
    i=0
    Y=0
    l=n-1
   
    while i<n:
        Y=((c[i])*(X**(l)))+Y
        i=i+1
        l=l-1
    print(Y)    

x=np.array([96,105],float)
y=np.array([114,125],float)
X=100

interpolação(x,y,X)
