def dpChangeMoney(money, coins):
    minnumcoins = (money + 1) * [0]
    for m in range(1, money + 1):
        minnumcoins[m] = m + 1  # basically the same as Inf since coins can't be <= 0
        for coin in coins:
            if m >= coin:
                if minnumcoins[m - coin] + 1 < minnumcoins[m]:
                    minnumcoins[m] = minnumcoins[m - coin] + 1
    return minnumcoins[money]
print(dpChangeMoney(40,[1,5,10,15,20,25,50]))
print(dpChangeMoney(17109,[1,3,5,7,8,23]))