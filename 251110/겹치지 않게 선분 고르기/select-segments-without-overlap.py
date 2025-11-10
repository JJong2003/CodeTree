n = int(input())
X = [list(map(int, input().split())) for _ in range(n)]
X.sort(key=lambda x:(x[1]-x[0], x[0], x[1]))

check = [False] * 1001

cnt = 0
for l, r in X:
    for i in range(l, r+1):
        if check[i]:
            break
    else:
        cnt += 1
        for i in range(l, r+1):
            check[i] = True
print(cnt)