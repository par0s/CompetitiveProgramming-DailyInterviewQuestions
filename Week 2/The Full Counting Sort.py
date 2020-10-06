def countSort(arr):
    l = len(arr)
    mid = l // 2

    print(arr)
    for i in range(mid):
        arr[i] = [arr[i][0],"-"]
    print(arr)

    dicts = {}
    maxVal = -1
    for i in range(l):
        c = arr[i][0]
        maxVal = max(maxVal,c)
        letter = arr[i][1]
        if c in dicts:
            dicts[c].append(letter)
        else:
            dicts[c] = [letter]
    
    answer = ""
    for i in range(maxVal + 1):
        if i in dicts:
            for chars in dicts[i]:
                answer += chars
    
    print(answer)
    return answer


arr = [[0,'a'],[1,'b'],[0,'c'],[1,'d']]
countSort(arr)