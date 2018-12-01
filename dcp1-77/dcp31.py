#Computer the distance between two strings.
#Distance equates to the transformation steps to make two strings equivalent
#Start time: 12:07
#GO

#So, what would the best approach be?
#Probably first to analyze the lengths of each string

def string_distance(s1, s2)->int:
    #What can we do if we have the length of each string? At least we can find the maximum distance
    #The maximum distance would automatically be the difference of the length of the strings
    #   plus the number of characters in a string

    # length_difference = abs(len(s1) - len(s2))
    #However, i think we can analyze this like a pathing problem. We need to find the optimal
    #   solution where the two strings line up.
    # return length_difference + min(len(s1), len(s2))

    #How much effort does the program have to do, if you were to build a new string from
    #   scratch, then subtract the highest order sequential matching count
    #So, let's do that. Let's find the largest similarity sequence between the two strings
    pass

def longest_matching_sequence(s1, s2):
    #Recursively return the largest matching sequence in that path
    if not len(s1) or not len(s2):
        return max(len(s1), len(s2))

    return min(longest_matching_sequence(s1[1:], s2)+1, 
               longest_matching_sequence(s1, s2[1:])+1, 
               longest_matching_sequence(s1[1:], s2[1:]) if s1[0] == s2[0] else \
               longest_matching_sequence(s1[1:], s2[1:]) + 1)

def min_string_distance(s1, s2):
    #Use memoization to do this, so we don't have to repeat so many complex and exponentially deep recursive calls
    #This is their solution, involving a (X x y) matrix to keep track of past computations
    x = len(s1) + 1
    y = len(s2) + 1

    memo = [[-1 for i in range(x)] for j in range(y)]

    #Now let's set the base values
    #These are the amount of work to go from an empty string to a string of string[:i]
    #So that makes sense where that work would translate to [0, 1, ..., n] work
    for i in range(x):
        memo[0][i] = i

    for j in range(y):
        memo[j][0] = j
    #So in terms of memoization, we're treating this like a pathfinding problem
    #The shortest path to [i,j] is +1 from the shorter of the left or top grid
    #But, if the character at i is the character at j, we don't have to do work, so
    #   therefore we only take the shorter of the left or top grid
    for i in range(1, y):
        for j in range(1, x):
            if s1[j-1] == s2[i-1]:
                memo[i][j] = min(memo[i-1][j], memo[i][j-1], memo[i-1][j-1])
            else:
                memo[i][j] = min(memo[i-1][j]+1, memo[i][j-1]+1,memo[i-1][j-1]+1)
    #Run a quick print of the matrix, for debugging and vizualization of the pathing
    for i in range(y):
        for j in range(x):
            print(f'{memo[i][j]:<3} ',end='')
        print()
    return memo[y-1][x-1]

    

if __name__ == "__main__":
    s1 = "sitting"
    s2 = "kitten"
    print(longest_matching_sequence(s1, s2))
    print(min_string_distance(s1, s2))
    s1 = "skiis"
    s2 = "kills"
    print(longest_matching_sequence(s1, s2))
    print(min_string_distance(s1, s2))
    #Complete by 2:20
    #Both work well, but the 2nd definitely is a lot faster and memory efficient