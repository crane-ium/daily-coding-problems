from random import randint
from collections import defaultdict

class tosser(object):
    def __init__(self, min=40, max=40):
        self.base_rand = randint(min,max)
    def toss_biased(self):
        rn = randint(1, 100)
        return 0 if rn <= self.base_rand else 1
    def toss_unbiased(self):
        toss_one = self.toss_biased()
        toss_two = self.toss_biased()
        if(toss_one != toss_two):
            if(toss_one):
                return True
            else: return False
        else: return self.toss_unbiased()

if __name__ == "__main__":
    coin_toss = tosser()
    coin_stats = defaultdict(int)
    for _ in range(1000000):
        coin_stats[coin_toss.toss_unbiased()] += 1
    print(coin_stats)
    