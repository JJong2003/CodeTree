n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

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
        return False # 사이클 없음
    return True     # 사이클 발생

for i in range(len(edges)):
    x, y = edges[i]
    result = _union(x, y)
    if result:
        print(i+1)
        break
else:
    print("happy")
