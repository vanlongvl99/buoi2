def getSums(sums,arrNums):
    sumFirst = 0
    sumSecond = 0
    left = 0
    right = nums - 1
    for i in range(nums):
        if (i % 2) ==0:
            if arrNums[left] > arrNums[right]:
                sumFirst = sumFirst + arrNums[left]
                left += 1
            else:
                sumFirst = sumFirst + arrNums[right]
                right = right - 1
        else:
            if arrNums[left] > arrNums[right]:
                sumSecond = sumSecond + arrNums[left]
                left += 1
            else:
                sumSecond = sumSecond + arrNums[right]
                right = right - 1
    return sumFirst,sumSecond
if __name__ == "__main__":
    nums = int(input())
    arrNums = list(map(int,input().split()))
    first, second = getSums(nums,arrNums)
    print(str(first),str(second))