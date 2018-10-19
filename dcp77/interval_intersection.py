#This takes a set of tuple intervals and merges any intersecting intervals

class IntervalMerger(object):
    """Store and merge intervals"""
    def __init__(self, *argv):
        self.arr = set([])
        for arg in argv:
            self._merge(arg)
    def add(self, *args):
        for tup in args:
            self._merge(tup)
    def _merge(self, tup:tuple):
        #Iterate through and merge where necessary
        if len(tup) != 2:
            exit
        if tup[0] > tup[1]:
            exit
        removeintervals = set([])
        flag = False
        tuparr = [tup[0], tup[1]]
        for interval in self.arr:
            flag = False
            if interval[0] <= tup[0]:
                if interval[1] >= tup[1]:
                    exit #The interval encompasses tup
                elif interval[1] >= tup[0]:
                    flag = True
                    tuparr[0] = interval[0]
            if interval[1] >= tup[1]:
                if interval[0] <= tup[1]:
                    flag = True
                    tuparr[1] = interval[1]
            elif interval[1] <= tup[1] and interval[0] >= tup[0]:
                removeintervals.add(interval)
            if(flag):
                removeintervals.add(interval)
        self.arr -= removeintervals
        self.arr.add(tuple(tuparr))
    def __str__(self):
        output = ""
        for interval in self.arr:
            output += f"{interval}"
        return output

# class IntervalIntersection(object):
#     #This one differs by using a more discrete method of checking interval intersections
#     def __init__(self, *argv):
#         self.intervals = set()
#         for arg in argv:
#             self.merge(arg)
#     def merge(self,tup:tuple):
#         if len(tup) != 2:
#             exit
#         if tup[0] > tup[1]:
#             exit
#         #We're going to turn these into real interval sets, which includes all integers between
#         interval1, interval2 = set(), set()
#         i1_range = [tup[0],tup[1]]
#         for val in range(tup[0],tup[1]+1):
#             interval1.add(val)
#         for interval in self.intervals:
#             interval2.clear()
#             for val in range(interval[0],interval[1]+1):
#                 interval2.add(val)
#             interval1 = interval1 | (interval1 ^ interval2)
            


if __name__ == "__main__":
    print(f"Hello, World!")
    intmerge = IntervalMerger((1,3),(5,8),(4,10),(20,25))
    intmerge.add((25,30))
    print(intmerge)

