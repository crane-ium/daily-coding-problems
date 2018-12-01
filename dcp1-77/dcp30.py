#We are given an array such that each integer represents an elevation
#If each number is an elevation, such that of a mountain, find out how much water can be poured
#   for each index in between to not flow over the boundaries

#Return a list of that corresponds to the original list, giving water capacity of each index
#EDIT: JK, it returns capacity of water on the map
def water_capacity(input:list)->int:
    #Let's go from the right and left simultaneously, because
    #   ultimately the left and right are the deciding 

    #Let's find the greatest value in the given array
    greatest_index = 0
    greatest = 0
    for i, x in enumerate(input):
        if x > greatest:
            greatest = x
            greatest_index = i

    water = 0
    #Iterate from left wall to the greatest, we can easily trace the water quantity
    left = 0
    for i in range(0, greatest_index):
        if input[i] > input[left]:
            left = i
            continue
        water += input[left] - input[i]
    right = 0
    for i in range(len(input)-1, greatest_index-1, -1):
        if input[i] > input[right]:
            right = i
            continue
        water += input[right] - input[i]
    return water

if __name__ == "__main__":
    list1 = [3, 0, 1, 2, 3, 0, 5]
    list2 = [2, 1, 2]
    print(f'{list1} water\'s capacity: {water_capacity(list1)}')
    print(f'{list2} water\'s capacity: {water_capacity(list2)}')
    #Okay, works!