#Given a list containing integers, where each element appears twice, except TWO appears once
#Find the two elements that appears once
#This is to be done linear time and constant space
#I think this is easy regardless if not for the constant space
#The constant space is what makes this fun and interesting!

#I remember this! There was a similar DCP. The trick is to use xor bitwise functions on the list

def find_singleton(arr:list):
    """Return the two items in the list that occurs once"""
    xorval = 0
    for num in arr:
        xorval ^= num
    #Now we have the two desired numbers xor'd, held in symbol 'xorval'
    #The bits in xorval that are marked 1, are bits that either existed in
    #   one but not the other. This means we can find where there's a difference
    #Here we can get the rightmost bit using two-'s complement
    xorval = xorval & -xorval
    sets = [0, 0]
    for num in arr: #we are going to categorize numbers that match the rightmost bit
        if num & xorval: #Means the rightmost bit exists in num also
            sets[0] ^= num
        else:
            sets[1] ^= num
    return (sets[0], sets[1]) #Returns a tuple containing the two elements

if __name__ == "__main__":
    #Let's test our function
    lst = [2, 4, 6, 8, 10, 2, 6, 10] #Given test value
    val1, val2 = find_singleton(lst)
    print(f'Value 1: {val1}\nValue 2: {val2}')

if __name__ == "__main__":
    pass
