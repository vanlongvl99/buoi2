def getMaxLine(nums,arrNums):
    maxline = 0
    flag1 = 1  # flag kiểm tra đã duyệt đến cuối chuỗi
    left = 0
    k = 0
    while left < nums:
        flag2 = 1  
        cnt = []
        cnt.append(arrNums[left])
        for j in range(left,nums):
            if arrNums[j] != arrNums[left] and flag2 == 1:   # kiểm tra để giảm số lần lặp while 
                flag2 = 0
                k = j
            if arrNums[j] not in cnt:   # duyệt số phần thử khác nhau trong khoảng đang xét
                cnt.append(arrNums[j])
            if len(cnt) == 3:           # kiểm tra max - min > 1
                if maxline < (j - left):
                    maxline = j - left
                break
            if j == nums - 1:         # khi xét đến cuối chuỗi max - min vẫn <= 1
                if maxline < (nums - left):
                    maxline = nums - left
                flag1 = 0
                break
        left = k
        if flag1 == 0:
            break
    return maxline
if __name__ == "__main__":
    nums = int(input())
    arrNums = list(map(int,input().split()))
    maxLine = getMaxLine(nums,arrNums)
    print(maxLine)