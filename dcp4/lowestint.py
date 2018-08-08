"""
Prompt:

Asked by Stripe

Given an array of integers, find the first missing positive int in linear time and constant space. 
In other words, find the lowest positive int that does not exist in the array.
The array can contain dupes and neg nums as well

For example [3, 4, -1, 1] should give 2
[1, 2, 0] should give 3

Can modify the input array in-place
"""
#Thoughts:
#Sort it using a O(1) space complexity algorithm
#Then traverse the list and check for a jump of 2 where the number in between is >0

class NumFinder(object):

    def __init__(self, L:list):
        self.nums = L
        self.count = 0
        self.missing_int = 0

    def relocate_left(self):
        """Move negative numbers to the left side of the list"""
        self.count = 0
        for i in range(len(self.nums)):
            if self.nums[i] <= 0:
                temp = self.nums[self.count]
                self.nums[self.count] = self.nums[i]
                self.nums[i] = temp
                self.count += 1

    def relocate_right(self):
        """Move neg nums to the right side"""
        self.count = 0
        for i in range(len(self.nums)):
            if self.nums[i] <= 0:
                while(len(self.nums) - self.count > 0 and self.nums[-1 - self.count] <= 0):
                    self.count += 1
                if i >= len(self.nums) - self.count - 1:
                    break
                temp = self.nums[-1 - self.count]
                self.nums[-1 - self.count] = self.nums[i]
                self.nums[i] = temp
                self.count += 1

    def find_int_left(self):
        """Return the lowest positive int not in a relocated_left list"""
        for i in range(self.count, len(self.nums)): #Set the corresponding indeces to the negative value if it exists
            num = abs(self.nums[i])
            if len(self.nums) > self.count + num - 1:
                self.nums[self.count + num - 1] = -self.nums[self.count + num - 1]
        #Check for the first index with a positive num and that (index - self.count + 1) is the missing pos int
        #Unless there are none, the lowest missing pos int is len(self.nums) - self.count + 1
        for i in range(self.count, len(self.nums)): 
            if self.nums[i] > 0:
                self.missing_int = i - self.count + 1
                return self.missing_int
        self.missing_int = len(self.nums) - self.count + 1
        return self.missing_int

    def find_int_right(self):
        for i in range(len(self.nums) - self.count):
            num = abs(self.nums[i])
            self.nums[num - 1] = -self.nums[num - 1]
        for i in range(len(self.nums) - self.count):
            if self.nums[i] > 0:
                self.missing_int = i + 1
                return self.missing_int
        self.missing_int = len(self.nums) - self.count + 1
        return self.missing_int

    def process_left(self):
        self.relocate_left()
        return self.find_int_left()

    def process_right(self):
        self.relocate_right()
        return self.find_int_right()

    @property
    def nums_left(self):
        return self.missing_int

    @nums_left.setter
    def nums_left(self, L:list):
        self.nums = L.copy()
        return self.process_left()

    @property
    def nums_right(self):
        return self.missing_int

    @nums_right.setter
    def nums_right(self, L:list):
        self.nums = L.copy()
        self.process_left()

if __name__ == "__main__":
    L = [3, 4, -1, 2, 1, -2, -3, 0,7]
    x = NumFinder(L.copy())
    xx = x.process_right()
    print(xx)
    x.nums = L.copy()
    xx = x.process_left()
    print(xx)
    L = [1]
    x.nums_right = L
    print(x.nums_right)
    x.nums_left = L
    print(x.nums_left)
    
                


