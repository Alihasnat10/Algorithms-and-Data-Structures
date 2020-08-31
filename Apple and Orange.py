def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples = [i+a for i in apples]
    oranges = [j+b for j in oranges]
    sum_apples = 0
    sum_oranges = 0
    for k in range(len(apples)):
        if apples[k] >=s and apples[k] <=t:
            sum_apples += 1
        if oranges[k] >=s and oranges[k] <=t:
            sum_oranges += 1
    print(sum_apples)
    print(sum_oranges)


s = 7
t = 10
a = 4
b = 12
m = 3
n = 3
apples = [2, 3, -4]
oranges = [3, -2, -4]
countApplesAndOranges(s, t, a, b, apples, oranges)
