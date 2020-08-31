#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    lastAnswer = 0
    a = [[] for i in range(n)]
    array_result = []
    
    for i in queries:
        x = i[1]
        y = i[2]
        if i[0] == 1:
            seq = ((x ^ lastAnswer) % n)
            a[seq].append(y)
        elif i[0] == 2:
            seq = ((x ^ lastAnswer) % n)
            lastAnswer = a[seq][y]
            array_result.append(lastAnswer)
    return array_result

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    print('\n'.join(map(str, result)))
    print('\n')

