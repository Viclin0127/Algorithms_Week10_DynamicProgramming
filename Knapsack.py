# Dynamic progamming problem - Knapsack
# Given n items with weight, value and knapsack capacity
# Find the most valuable selection of items that will fit in the knapsack

def Knapsack(W, value, weight):
    n = len(value)
    K = []
    for i in range(n+1):
        K.append([0] * (W+1))           # create an empty 2D array with length len(value)+1 and W+1
    for i in range(1, n+1):
        for j in range(1, W+1):         # start from i = 1 and j = 1
            if j < weight[i-1]:         # if this item's weight is larger than j, it can't be in the knapsack
                K[i][j] = K[i-1][j]     # so we choose the last larger set in this j weight
            else:
                K[i][j] = max(K[i-1][j], K[i-1][j - weight[i-1]] + value[i-1])
                # if this item's weight is smaller than j,
                # there are 2 scenario, 1 is not select this item (which = K[i-1][j])
                # the other is select this item (=K[i-1][j - weight[i-1]] + value[i-1])
    return K[-1][-1]                    # return the last element

def test():
    W = 10
    value = [10,15,5,12]
    weight = [5,7,3,5]
    print(Knapsack(W, value, weight))

if __name__=="__main__":
    test()