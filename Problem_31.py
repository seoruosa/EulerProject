COINS = [1, 2, 5, 10, 20, 50, 100, 200]
TOTAL = 200


def combinationsCoins(summation, coins):
    countList = [0]*(summation+1)

    for coin in coins:
        for i in range(summation+1):
            if coin == i:
                countList[i] += 1
            if i>coin:
                countList[i] = (countList[i]+countList[i-coin])
    return countList[-1]

if __name__=='__main__':
    print(combinationsCoins(TOTAL, COINS))