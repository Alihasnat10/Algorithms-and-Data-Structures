def breakingRecords(scores):
    result =[0, 0]
    highest = scores[0]
    lowest = scores[0]
    for i in range(1, len(scores)):
        if scores[i] > highest:
            result[0] += 1
            highest = scores[i]
        if scores[i] < lowest:
            result[1] += 1
            lowest = scores[i]
    return result
if __name__ == '__main__':
    n = 9

    scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]

    result = breakingRecords(scores)

    print(' '.join(map(str, result)))
    print('\n')
