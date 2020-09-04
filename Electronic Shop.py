def getMoneySpent(k, d, b):
    sum = []
    max = -1
    for i in range(len(k)):
        for j in range(len(d)):
            sum.append(k[i] + d[j])
    for i in range(len(sum)):
        if sum[i] > max and sum[i] < b:
            max = sum[i]


    print(max)

b  = 5
keyboards = [4]
drives = [5]
getMoneySpent(keyboards, drives, b)
