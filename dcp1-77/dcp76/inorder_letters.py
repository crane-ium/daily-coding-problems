"""
inorder_letters:
-Takes a matrix m x n and removes columns that are not in an increasing order
"""

from random import randint
from collections import deque

def letter_matrix_generator(m:int,n:int):
    array = [[""]*m for _ in range(n)]
    for m, r in enumerate(array):
        for n, c in enumerate(r):
            temp = randint(0,25)
            array[m][n] = chr(ord('a') + temp)
    return array

def clean_matrix(arr:list):
    #So we will want to remove any column that ever decreases
    #Maybe running a binary search is fastest? I don't think it's any faster
    #How to beat worst case O(mn) time where no column is deleted?

    #Let's start by assuming this is a clean matrix of m x n size
    bad_c = deque([])
    for n in range(0, len(arr[0])):
        for m in range(1, len(arr)):
            if arr[m-1][n] >= arr[m][n]:
                print("Remove column", n)
                bad_c.append(n)
                break
    while len(bad_c) > 0:
        c = bad_c.pop()
        for m in range(0,len(arr)):
            del arr[m][c]
    return arr

if __name__ == "__main__":
    arr = letter_matrix_generator(20, 2)
    for i in range(0,len(arr)):
        print(arr[i])
    new_arr = clean_matrix(arr)
    for i in range(0,len(arr)):
        print(new_arr[i])
    