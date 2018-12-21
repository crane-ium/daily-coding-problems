from collections import OrderedDict
#Find the least required coins to reach a sum of n cents.
#We will use standard USA denominations of 25, 10, 5, 1

# CENTS = {25:'QUARTER', 10:'DIME', 5:'NICKEL', 1:'PENNY'}
# ORDEREDCENTS = OrderedDict(sorted(CENTS.items(), key=lambda x: x[0], reverse=True))
CENTS = {'QUARTER':25, 'DIME':10, 'NICKEL':5, 'PENNY':1}
ORDEREDCENTS = OrderedDict(sorted(CENTS.items(), key=lambda x: x[1], reverse=True))

def get_coin_count(totalcents, printcoins:bool = False):
    #We will iterate through the dictionary, largest key to smallest, to do modular arithmetic
    #   with the largest value denominations first
    centcounts = ORDEREDCENTS.copy()
    for item in ORDEREDCENTS.items():
        centcounts[item[0]] = totalcents // item[1]
        totalcents -= centcounts[item[0]] * item[1]
    # print(centcounts)
    coincount = sum([item[1] for item in centcounts.items()])
    if printcoins:
        print(f'Coin counts: {centcounts}')
    return coincount

if __name__ == "__main__":
    cents = 16
    count = get_coin_count(cents, True)
    print(f'Coins for {cents} cents: {get_coin_count(cents)}')