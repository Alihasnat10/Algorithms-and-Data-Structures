def miniMaxSum(arr):
    summation=[0]*5
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                summation[i]+=arr[j]

    print(min(summation), max(summation))


if __name__ == '__main__':
    arr = [5, 5, 5, 5, 5]

    miniMaxSum(arr)
