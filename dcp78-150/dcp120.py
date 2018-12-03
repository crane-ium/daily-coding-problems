#Find the smallest set of numbers that is included in all given intervals

from collections import OrderedDict
from collections import deque
from itertools import combinations, chain
from random import randint

def get_set(interval_list:list)->set:
    #Conclusion: This is an awfully structured implementation. But, it does get hte job done and it does use robust logic...
    combos = list(powerset(interval_list, 1)) #Get powerset
    # print(combos)
    intersections = []
    for i in range(4, 0, -1):
        for combo in filter(lambda x: len(x)==i, combos):
            intersect = get_intersection(combo)
            if(intersect): #Not empty list
                for s in powerset(combo, max=len(combo)-1):
                    try:
                        combos.remove(s)
                    except:
                        pass
                # print(combos)
                intersections.append(intersect)
                # print("Intersections: ", intersections)
    # print(intersections)
    #Now we need to filter out the excess, because we are only returning  a set of integers that are contained
    s = set()
    for x in intersections:
        if len(x) == 1:
            s.add(x[0])
        else:
            s.add(randint(x[0], x[1]))
    return s

    # intersected = [False for interval in interval_list]
    # intersectflag = false
    # unchecked = deque(interval_list)
    # newchecked = deque()
    # final = set() #Checked and doesn't intersect with others
    # #Now check for each interval, if it intersects with any other in the list
    # while unchecked:
    #     for interval in unchecked[1:]:
    #         next = get_intersection(interval)

def powerset(iterable, min=1, max=-1, length=-1):
    #Pretty cool method of getting a powerset
    s = list(iterable)
    if max==-1:
        max = len(s)
    if length != -1:
        min=length
        max=length
    return chain.from_iterable(combinations(s, r) for r in range(min, max+1))

#Returns the intersection of given intervals
def get_intersection(intervals)->list:
    intersection = []
    lowest = sorted([interval[0] for interval in intervals])
    highest = sorted([max(interval) for interval in intervals])
    if sorted([num for interval in intervals for num in interval]) == lowest+highest:
        intersection = list(OrderedDict.fromkeys([max(lowest), min(highest)]))
    return intersection

def given_solution(intervals):
    def intersecting(i1, i2):
        return not (min(i1) > max(i2) or min(i2) > max(i1))
    #So, doing this only from looking at the conceptual solution. Not code
    #We should sort the intervals. Here we will do by starting point
    intersections = set()
    i_first = list(sorted(intervals, key=lambda x: x[0]))
    print(i_first)
    i=0
    while i < len(i_first):
        interval = i_first[i]
        while i < len(intervals) and intersecting(interval, intervals[i]):
            interval = get_intersection([interval,i_first[i]])
            i+=1
        intersections.add(randint(min(interval), max(interval)))

    print(intersections)
    return intersections

def covering(intervals):
    intervals.sort(key=lambda x: x[0])

    result = []
    i = 0

    while i < len(intervals):
        interval = intervals[i]

        while i < len(intervals) and intersecting(intervals[i], interval):
            interval = (max(intervals[i][0], interval[0]), min(intervals[i][1], interval[1]))
            i += 1

        result.append(interval[1])
    return result

def intersecting(x, y):
    return not (x[0] > y[1] or y[0] > x[1])

if __name__ == "__main__":
    intervals1 = [[0, 3], [2, 6], [3, 4], [6, 9]]
    print("Intersection of first 3: ", get_intersection(intervals1[:3]))
    print("Intersection of first 2: ", get_intersection(intervals1[:2]))
    p = list(powerset(range(4)))
    # print(list(filter(lambda x: len(x)==2, p)))

    test = [1, 2, 3, 4]
    s = get_set(intervals1)
    print("Smallest set: ", s)
    s = covering(intervals1)
    print(s)