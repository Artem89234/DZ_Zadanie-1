from random import random
N = 5
a = []
k = []
l = 0
u = 0
y = []
for i in range(N):
    z = []
    for j in range(N):
        n = int(random()*100)
        print('%4d' % n, end='')
        z.append(n)
    print()
    a.append(z)
print()
l = a[2]
l1 = max(l)

for i in range(N):
    z = []
    for j in range(N):
        n = int(random()*100)
        print('%4d' % n, end='')
        z.append(n)
    print()
    k.append(z)
print()
u = k[2]
u1 = max(u)

if u1 > l1:
    t = u1
else:
    t = l1
for i in range(N):
    if a[2][i]==t:
        n1 = i
for i in range(N):
    if k[2][i]==t:
        n1 = i
        
for i in range(N):
    z = []
    for j in range(N):
        n = int(random()*100)
        z.append(n)
    y.append(z)
y[2][n1] = t 

for i in range(N):
    for j in range(N):
        n2 = y[i][j]
        print('%4d' % n2, end='')
    print()












