n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 2)]

uf = [i for i in range(n+1)]

def _find(x):
    if uf[x] != x:
        uf[x] = _find(uf[x])
    return uf[x]

def _union(a, b):
    x = _find(a)
    y = _find(b)

    if x != y:
        uf[x] = y

for x, y in edges:
    _union(x, y)

# 서로 다른 집합을 찾는다(root)
for i in range(1, n+1):
    
    for j in range(i, n+1):
        if _find(uf[i]) != _find(uf[j]):
            print(i, j)
            exit(0)
            