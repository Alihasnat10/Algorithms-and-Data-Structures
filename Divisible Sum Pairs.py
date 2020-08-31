def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(len(ar)):
        for j in range(len(ar)):
            if i <j  and (((ar[i] + ar[j]) % k) == 0):
                count += 1
    return count

if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    print(str(result) + '\n')
