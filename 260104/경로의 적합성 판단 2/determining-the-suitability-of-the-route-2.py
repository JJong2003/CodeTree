n, m, k = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(m)]
path = list(map(int, input().split()))

# Please write your code here.

uf = [i for i in range(n+1)]

def _find(a):
    if uf[a] == a:
        return a
    uf[a] = _find(uf[a])
    return uf[a]

def _union(a, b):
    pa = _find(a)
    pb = _find(b)
    
    uf[pb] = pa

for edge in edges:
    a, b = edge
    _union(a, b)

for i in range(len(path) - 1):
    if _find(path[i]) != _find(path[i+1]):
        print(0)
        break
else:
    print(1)