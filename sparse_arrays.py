def matchingStrings(strings, queries):
    result = [0] * len(queries)
    for i in range(len(queries)):
        for j in range(len(strings)):
            if strings[j] == queries[i]:
                result[i] += 1
    return result


strings = ['aba', 'baba', 'aba', 'xzxb']
queries = ['aba', 'xzxb', 'ab']
r=matchingStrings(strings, queries)
for i in r:
    print(i,end=' ')
