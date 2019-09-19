def getVest(n,m,x,y,a,b):
    indexA = 0
    indexB = 0
    arr = []
    while indexA < n and indexB < m:
        if a[indexA] - x <= b[indexB] and b[indexB] <= a[indexA] + y:
            indexA += 1
            indexB += 1
            arr.append(str(indexA) + " " + str(indexB))
        elif  b[indexB] < a[indexA] - x:
            indexB += 1
        else:
            indexA += 1
    return arr
if __name__ == "__main__":
    n,m,x , y    = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    arr = getVest(n,m,x,y,a,b)
    print(len(arr))
    for i in range(len(arr)):
        print(arr[i])