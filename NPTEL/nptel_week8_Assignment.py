n,k = map(int,input().split())
l = []
l.append(0)

for i in range(n):
    x = int(input())
    l.append(x)

best = [[0 for z in range(k+1)] for zz in range(n+1)]

for i in range(1, n+1):
    best[i][0] = max(best[i-1][0]+l[i], l[i])

    for j in range(1, min(i+1, k+1)):
        best[i][j] = max(best[i-1][j]+l[i], best[i-1][j-1])

ans = 0
for i in range(1, n+1):
    ans = max(ans, best[i][k])

print(ans)