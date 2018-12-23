#Create a wrapper iterator

class PeakableInterface(object):
    def __init__(self, iterator):
        self.it = iterator #Holdthe iterator
        # self.index = 0 #Initial index of the iterator
        self._next = next(self.it) #Instead of indexing, just use the iterator's builtin iter functions
    
    def peek(self):
        #Return the next value in the iterator without incrementing
        return self._next

    def next(self):
        #Return the next value in the iterator while iterating
        return_val = self._next #Hold the next val temporarily
        try:
            self._next = next(self.it) #Get the next in the iterable
        except:
            self._next = None #Test if the iterable can handle the next, otherwise set it to None
        #Is this try/except bad practice? I feel like it's cheating
        return return_val 

    def hasNext(self):
        #Return t/f if there is a next value in the iterator
        return not self._next is None #If the next value of self.it has more?
    
if __name__ == "__main__":
    #Create an iterable
    lst = [1, 2, 3, 4]
    myit = PeakableInterface(iter(lst))
    while(myit.hasNext()):
        print(f'Peeking: {myit.peek()} \nNext val: {myit.next()}')