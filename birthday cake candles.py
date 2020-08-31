def birthdayCakeCandles(ar):
    max = 0
    for i in ar:
        if i>max:
            max = i
    count = 0
    for i in ar:
        if i == max:
            count+=1
    print(count)


ar = [4, 4, 1, 3,5,5,5,7,7]
birthdayCakeCandles(ar)
