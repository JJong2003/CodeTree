n, m = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(m)]

# Please write your code here.
array = [i for i in range(n + 1)]


def _find(a):
    if array[a] != a:
        array[a] = _find(array[a])
    return a


def _union(a, b):
    pa = _find(a)
    pb = _find(b)

    array[pa] = pb


for i in range(m):
    cmd, a, b = query[i]
    if cmd == 0:
        _union(a, b)
    else:
        print(1 if _find(a) == _find(b) else 0)