def matchingStrings(strings, queries):
    occur = {}
    for i in strings:
        if i in occur:
            occur[i] += 1
        else:
            occur[i] = 1
    
    ans = []
    for i in queries:
        if i in occur:
            ans.append(occur[i])
        else:
            ans.append(0)
    
    return ans