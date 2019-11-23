from random import random
N = 5
M = 10
a = []
for i in range(N):
    z = []
    for j in range(M):
        n = int(random()*15)-15
        print('%4d' % n, end='')
        z.append(n)
    print()
    a.append(z)
print()

for i in range(N):
    i = i + 1
    if i%2==0:
        i = i - 1
        print(a[i])
        for j in range(M):
            j = j + 1
            if j%2==0:
                j = j - 1
                print(a[i][j])