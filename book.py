def getBooks(n,t,arrMinutes):
    amount = []
    count = 0
    sumMinute = 0
    for i in range(n):
        if sumMinute + arrMinutes[i] <= t:
            sumMinute = sumMinute + arrMinutes[i]
            count += 1   # số quyển sách có thể đọc đc bắt đầu từ n0
        else:
            break
    if count == n:
        return print(count)
    left = 0
    amount.append(count)
    for i in range(count,n):   # tránh trường hợp không có sách nào đc đọc
        sumMinute = sumMinute + arrMinutes[i]
        while sumMinute > t
            sumMinute = sumMinute - arrMinutes[left]
            left = left + 1
        amount.append(i - left + 1)
    return max(amount)

if __name__ == "__main__":
    n, t = map(int,input().split())
    arrMinutes = list(map(int,input().split()))    
    result = getBooks(n,t,arrMinutes)
    print(result)