from heapq import heappop, heappush

n, m = map(int, input().split())
uf = [i for i in range(n+1)]

def _find(x):
    if uf[x] != x:
        uf[x] = _find(uf[x])
    return uf[x]

def _union(a, b):
    pa = _find(a)
    pb = _find(b)
    if pa != pb:
        uf[pb] = pa

h = []
for _ in range(m):
    a, b, weight = map(int, input().split())
    heappush(h, (weight, a, b))

ans = 0
for i in range(m):
    weight, a, b = heappop(h)
    if _find(a) != _find(b):
        _union(a, b)
        ans += weight
print(ans)