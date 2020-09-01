#Find the maximum number of bird with its id
def migratoryBirds(arr):
    unique = []
    for i in arr:
        if i not in unique:
            unique.append(i)
    count = [0] * len(unique)
    for i in range(len(unique)):
        for j in range(len(arr)):
            if unique[i] == arr[j]:
                count[i] += 1
    max = 0
    index = 0
    for i in range(len(count)):
        if count[i] > max:
            max = count[i]
            index = i
        if count[i] == max and unique[i] < unique[index]:
            max = count[i]
            index = i


    return unique[index]



arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4, 1]
migratoryBirds(arr)
