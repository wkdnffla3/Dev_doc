temp = [[[] for _ in range(10)]for _ in range(10)]
temp[0]=1
print(temp)

tmp = [[0]]*10
tmp[0][0] = 1
tmp[0].append(10)
print(tmp)

tmp2 = [0]*10
tmp2[0] = 1
print(tmp2)

from time import time
 
 
def check():
    start = time()
    for i in range(10 ** 8):
        pass
    return time() - start
 
 
print(check())
start = time()
for i in range(10 ** 8):
    pass
print(time() - start)