n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
indexA = 0
indexB = 0
while indexB < m:
    if indexA == n:
        break
    if a[indexA] <= b[indexB]:
        indexA += 1
    indexB += 1
print(n - indexA)