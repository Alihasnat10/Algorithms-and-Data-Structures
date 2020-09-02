def sockMerchant(n, ar):
    count = 0
    unique = []
    num = 0
    for i in range(len(ar)):
        if ar[i] not in unique:
            unique.append(ar[i])
    count = [0] * len(unique)
    for i in range(len(unique)):
        for j in range(len(ar)):
            if unique[i] == ar[j]:
                count[i] += 1
    for i in range(len(count)):
        while count[i] > 1:
            count[i] -= 2
            num += 1

    print(num)
n=9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
sockMerchant(n, ar)
