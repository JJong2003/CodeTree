n = int(input())

# Please write your code here.
parent = {}
for _ in range(n-1):
    s, e = map(int, input().split())
    parent[e] = s

for i in range(2, n+1):
    print(parent[i])

print(parent)