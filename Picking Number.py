def pickingNumbers(a):
    # Write your code here
    a.sort()
    ans = []
    count = []
    for i in range(len(a)):
        ans = []
        for j in range(i, len(a)):
            if abs(a[i] - a[j]) <= 1:
                ans.append(a[j])
            else:
                break
        count.append(len(ans))
    return max(count)

if __name__ == '__main__':
    a = [1,2,2,3,1,2]

    result = pickingNumbers(a)

    print(str(result) + '\n')
