def truckTour(petrolpumps):
    #
    # Write your code here.
    #
    miner = 0
    n = len(petrolpumps)
    for i in range(1,n):
        inc = petrolpumps[i - 1][0] - petrolpumps[i - 1][1]
        if inc < 0:
            miner = i
        else:
            petrolpumps[i][0] += inc
    
    return miner