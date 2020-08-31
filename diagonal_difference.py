arr=[[11, 2, 4],
     [4, 5, 6],
     [10, 8, -12]]
left_diagonal = 0
right_diagonal = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if i == j:
            left_diagonal += arr[i][j]
        if (i+j) == (len(arr) - 1):
            right_diagonal += arr[i][j]

diff =  abs(right_diagonal - left_diagonal)
print(diff)


