import sys
input = sys.stdin.readline

n, m = map(int, input().split())

uf = [i for i in range(n+1)]
size = [1 for i in range(n+1)]

def _find(a):
    if uf[a] == a:
        return a
    uf[a] = _find(uf[a])
    return uf[a]

def _union(a, b):
    pa = _find(a)
    pb = _find(b)

    if size[pa] < size[pb]:
        uf[pa] = pb
        size[pb] += size[pa]
    else:
        uf[pb] = pa
        size[pa] += size[pb]


for _ in range(m):
    op, *nums = input().split()
    if op == "x":
        a, b = map(int, nums)
        _union(a, b)
    else:
        a = int(nums[0])
        sys.stdout.write(str(size[_find(a)]) + "\n")
sys.stdout.flush()