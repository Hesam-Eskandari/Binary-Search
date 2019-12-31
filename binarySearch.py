# Binary Search (BS)
from random import randint
import numpy as np
from time import time
import matplotlib.pyplot as plt
from math import log

def binary_search(a,x,ind=0):
    if len(a)>=2:
        mid = len(a)//2
        y = a[mid]
        if x == y:
            return y,ind+mid
        elif x > y:
            return binary_search(a[mid+1:],x,ind+mid+1)
        elif x < y:
            return binary_search(a[:mid],x,ind)
    elif x == a[0]:
        return x,ind

############################
times = []
lengths = [100000 for n in range(100)]
indices = [];correct=[];l=[]
for length in lengths:
    #print(length)
    a = [randint(1,3*10**9) for i in range(length)]
    x = a[randint(0,length-1)]
    a.sort()
    t1 = time()
    bs = binary_search(a,x)
    t2 = time()
    if bs:
        [y,ind] = bs 
    else:
        print('bug report: returned none')
        continue
    
    times.append(t2-t1)
times_avg = sum(times)/len(times)
    
#########################
times = []
lengths = [10000*(n+10) for n in range(65)]
indices = [];correct=[];l=[]
for length in lengths:
    #print(length)
    a = [randint(1,3*10**9) for i in range(length)]
    
    x = a[length//2]
    x = a[randint(0,length-1)]
    a.sort()
    t1 = time()
    bs = binary_search(a,x)
    t2 = time()
    if bs:
        [y,ind] = bs 
    else:
        print('bug report: returned none')
        continue
    
    indices.append(ind)
    correct.append(x-a[ind])
    times.append((t2-t1)/2.5)
    l.append(length)
    
print("Correctness:",sum(correct)==0)
n = [(i+1)*times_avg for i in range(len(times))]
nlog = [log((i+2),2)*times_avg for i in range(len(times))]
plt.plot(l,times,label="bs")
plt.plot(l,n,'-ro',label="n")
plt.plot(l,nlog,'-g*',label="log(n)")
plt.legend(loc="upper left")
plt.xlabel('Size of Array')
plt.ylabel('Time')
#plt.savefig('BS.png',dpi=500)
plt.show()
