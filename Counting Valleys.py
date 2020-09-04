def countingValleys(n, s):
    sea = 0
    v = [0]
    count = 0
    for i in s:
        if i == 'U':
            sea += 1
            v.append(sea)
        elif i == 'D':
            sea -= 1
        v.append(sea)
    for i in range(len(v)-1):
        if v[i] == 0 and v[i+1] == -1:
            count+=1
    print(count)



n = 12
s='DDUUDDUDUUUD'
countingValleys(n, s)
