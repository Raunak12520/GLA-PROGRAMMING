import numpy as np
r,c=map(int,input().split())
ls1=list(map(int,input().split()))
ls2=list(map(int,input().split()))
m1=np.array(ls1).reshape(r,c)
m2=np.array(ls2).reshape(r,c)
out=np.add(m1,m2)
print(out)
