
#Looking at this, we don't need to account for obstacles
#And moving diagonal is 1 step
#So the optimal path from current to dest is the greater of the changes in x and y

def travel_steps(l: list):
    x = l[0][0]
    y = l[0][1]
    steps = 0
    for coord in l[1:]:
        #Gives us a tuple of x-y coords
        steps += max(abs(coord[0]-x), abs(coord[1]-y))
        x = coord[0]
        y = coord[1]
    return steps

def given_solution_one(X: list, Y: list):
    #Their solution was in C++ btw, so transposing
    distance = 0
    def get_distance(xin, xf, yin, yf):
        steps = 0
        x0 = xin
        y0 = yin
        while x0 != xf or y0 != yf:
            if x0 != xf:
                x0 += (xf - x0)/abs(xf - x0)
            if y0 != yf:
                y0 += (yf - y0)/abs(yf - y0)
            steps += 1
        return steps
    for xi, yi in zip(range(1, len(X)), range(1, len(Y))):
        distance += get_distance(X[xi-1], X[xi], Y[yi-1], Y[yi])
    return distance

if __name__ == "__main__":
    travel_list = list()
    travel_list = [(0,0), (1, 1), (1, 2), (3, 6), (-6, -2)]
    print(f'It took {given_solution_one([c[0] for c in travel_list], [c[1] for c in travel_list])} steps to get from ')
    # print([c[0] for c in travel_list])
    # for i, coord in enumerate(travel_list):
        # print(f'{i}: {coord} ', end=' ')
    # print()
    for pt in travel_list[:-1]:
        print(pt, " to ", end=' ')
    print(travel_list[-1])

#Final notes:
#-My function matched their function's concept identitcally
#-Included their other solution which was to move step by step