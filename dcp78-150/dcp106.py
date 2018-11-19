
#Given an array of integers, see if there's a path of hopping to reach the final index

def is_array_hoppable(array: list):
    #The best way is to backtrack with memoization
    path = [False]*(len(array)-1) + [True] #Matches with the final index of the given list
    for i in range(1, len(array)):
        hops = array[len(array) - 1 - i]
        current_i = len(array) - 1 - i
        for hoppy in range(1, hops + 1):
            if(current_i + hoppy < len(array) and path[current_i + hoppy]):
                path[current_i] = True
                #Uses backtrack from the end towards the start to find if that path is hoppable
    #This Solution is O(n) time and O(n) space complexity
    # print(f'Hop path: {path}')
    return path[0]

if __name__ == "__main__":
    lists = [
        [2, 0, 1, 3, 0, 0, 5, 0, 1, 0, 0],
        [1, 1, 0, 1]
    ]
    for lst in lists:
        print(f'Is hoppable? {"Yes" if is_array_hoppable(lst) else "No"}')