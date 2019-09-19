num,k = map(int,input().split())
listnum = list(map(int,input().split()))
cnt = [0]*100001
count = 0
for i in range(num):
    cnt[listnum[i]] = cnt[listnum[i]] + 1
    if cnt[listnum[i]] == 1:￼￼
        count += 1
    if count == k:
        right = i
        break
if count != k:
    print("-1 -1")
else:
    for i in range(right+1):
        if cnt[listnum[i]] > 1:
            cnt[listnum[i]] = cnt[listnum[i]] - 1
        else:
            print(str(i + 1),str(right + 1))
            exit()