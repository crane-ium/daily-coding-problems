#Create a bit array

class bit_arr(object):
    def __init__(self, size=0):
        self.size = size
        self.array = list([False]*size)
        self.outofupperbound = 'bit_arr OutOfBounds: i should not be greater than size of {}'.format(self.size)
        self.outoflowerbound = 'bit_arr OutOfBounds: i should be greater than or equal to 0'
    def set(self, i, val:bool):
        if i >= self.size:
            raise Exception(self.outofupperbound)
        elif i < 0:
            raise Exception(self.outoflowerbound)
        self.array[i] = val
    def get(self, i):
        if i >= self.size:
            raise Exception(self.outofupperbound)
        elif i < 0:
            raise Exception(self.outoflowerbound)
        return self.array[i]

if __name__ == "__main__":
    ba = bit_arr(10)
    ba.set(3, True)
    print(ba.get(3))
    print(ba.get(4))
    print(ba.get(9))
    try:
        print(ba.get(10))
    except:
        print('Failed to get the thingy')
    try:
        print(ba.set(-1, True))
    except:
        print('Failed to set the thingy')
