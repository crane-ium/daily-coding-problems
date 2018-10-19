from random import randrange

class RNG:
    def rand5(self):
        return (randrange(1,6))
    def rand7(self):
        def l3():
            x = self.rand5() - 1
            while(x > 2):
                x = self.rand5() - 1
            return x
        x,y = l3(), l3()
        z = x + y * 3 + 1
        while(z > 7):
            x,y = l3(), l3()
            z = x + y * 3 + 1
        return z
    def sim_dist(self):
        f = self.rand7
        rand_arr = [0]*7
        total_runs = 100000
        for _ in range(0,total_runs):
            i = f() -1
            rand_arr[i] = rand_arr[i] + 1
        totes = 0
        for x in rand_arr:
            totes += x
        print(f'Totes: {totes}')
        for i, n in enumerate(rand_arr):
            print(f'{i+1} occurences: {n:>5}  : {n/totes*100:>5.4}% +- {abs(1/7 - n/totes)*100:.5}')


if __name__ == "__main__":
    r = RNG()
    r.sim_dist()

