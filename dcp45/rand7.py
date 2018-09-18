from random import randrange

class RNG:
    def rand5(self):
        return (randrange(1,6))
    def rand7(self):
        x = self.rand5()
        assert(x<=5 and x>=1)
        y = self.rand5() - 1
        while(y >= 3):
            y = self.rand5() - 1
        assert(y<=2 and y>=0)
        return x + y
    def sim_dist(self):
        f = self.rand7
        rand_arr = [0]*9
        total_runs = 10000
        for _ in range(0,total_runs):
            rand_arr[f()] = rand_arr[f()] + 1
        totes = 0
        for x in rand_arr:
            totes += x
        print(f'Totes: {totes}')
        for i in range(1,8):
            print(f'{i} occurences: {rand_arr[i]}  %: {rand_arr[i]/totes}')


if __name__ == "__main__":
    r = RNG()
    r.sim_dist()

