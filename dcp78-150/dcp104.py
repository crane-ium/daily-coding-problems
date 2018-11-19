from random import randint
#Return T/F if a linked list is palindromic

class node(object):
    def __init__(self, num: int = None, n = None):
        self.next = n
        self.val = num
    def insert_list(self, l: list):
        for n in l:
            self.insert(n)
    def insert(self, num: int):
        if not isinstance(num, int):
            raise TypeError
        if self.val is None:
            self.val = num
            return
        self.next = node(self.val, self.next)
        self.val = num
    def __str__(self):
        if self.val is None:
            return None
        return f'{self.val} {f" -> {self.next}" if self.next else f""}'
    def __iter__(self):
        self.ptr = self
        return self.ptr
    def __next__(self):
        if self.ptr:
            temp = self.ptr
            self.ptr = self.ptr.next
            return temp
        else:
            raise StopIteration
    def yield_all(self):
        ptr = self
        while ptr:
            if ptr.val is not None:
                yield ptr.val
            ptr = ptr.next
    
def is_palindromic(ll: node) -> bool:
    #One approach would be to xor all the values together and keep track of the middle value
    # total_xor = 0
    # count = 0
    # middle = n
    # ptr = n
    # while ptr != None:
    #     total_xor ^= ptr.val
    #     count+=1
    #     if count % 2 and count != 1:
    #         middle = middle.next
    #     ptr = ptr.next
    # print(f'count: {count} total_xor: {total_xor}')
    # if (count+1) % 2:
    #     print('ya')
    #     return not bool(total_xor)
    # else:
    #     print('na')
    #     return middle.val == total_xor
    #OKAY....THAT WAS AWFUL, failing for obvious reasons
    #Let's try again
    nums = ll.yield_all()
    nums_rev = reversed(list(ll.yield_all()))
    return all(x == y for x, y in zip(nums, nums_rev))

if __name__ == "__main__":
    l1 = [1, 2, 3, 2, 1]
    l2 = [3, 2, 6, 6, 2, 3]
    l3 = [5, 4, 5, 4]
    l4 = [1, 2, 3, 4, 5]
    l5 = [5, 4, 5, 4, 0]
    lists = [l1, l2, l3, l4, l5]
    for l in lists:
        n = node()
        n.insert_list(l)
        print(n)
        print(f'Palindrome: ', 'Yes' if is_palindromic(n) else 'No')
        