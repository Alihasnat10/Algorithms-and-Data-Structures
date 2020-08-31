def staircase(n):
    for i in range(n):
        for j in range(n,i+1,-1):
            print(' ',end='')
        print('x'*(i+1))

staircase(4)
