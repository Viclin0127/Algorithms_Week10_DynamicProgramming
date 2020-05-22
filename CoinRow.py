# Dynamic programming problem - The Coin-Row
# Given a row of coins, pick up largest sum with the constraint: no adjacent coins can be picked

def CoinRow(C):
    S = [0] * len(C)                # create an array to store max value
    S[0] = C[0]
    S[1] = max(C[0], C[1])          # since that we can not choose adjacent coins
    for i in range(2, len(C)):
        S[i] = max(S[i-1], S[i-2]+C[i])     # choose that particular coin or not, and find max value
    return S[-1]                    # return the last element


def test():
    C = [10, 20, 20, 30, 50, 20, 10]
    print(CoinRow(C))

if __name__=="__main__":
    test()
