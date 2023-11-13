import sys
n = int(input())
sys.setrecursionlimit((n+10)*10) 
a = list(map(int,input().split()))
f = [0] * (n+10)

def qhd(id):
    if id >= n: 
        return 0
    if f[id] != 0:
        return f[id]
    if n-id < 10:
        return 0
    elif n-id >= 10:
        f[id] = max(qhd(id+1), qhd(id+10) + min(a[id: id+10]))
    return f[id]

print(sum(a)-qhd(0))
