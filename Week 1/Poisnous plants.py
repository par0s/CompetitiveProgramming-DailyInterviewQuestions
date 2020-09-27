def poisonousPlants(p):
    res = 0
    n = len(p)    
    stack = []
    stack.append((p[0],0))
    for i in range(1,n):
        day_lasted = 1

        while(stack and stack[-1][0] >= p[i]):
            day_lasted = max(day_lasted,stack[-1][-1] + 1)
            print(stack)
            stack.pop()

        if len(stack) == 0:
            # doesn't die
            day_lasted = 0
        stack.append((p[i],day_lasted))
        res = max(res,day_lasted)
        
    return res

 
