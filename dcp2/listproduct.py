"""
Prompt:
This problem was asked by Uber

Given an array of integers, return a new array such that each element at index i of the new array is the product
of all the numbers in the original array except the one at i.

For example, if our input was
[1, 2, 3, 4, 5]
the expected output was be
[120, 60, 40, 30, 24].
If our input was
[3, 2, 1]
our output would be
[2, 3, 6]
"""

def get_product_list(L: list) -> list:
    """
    Returns a list of products of the all L elements excluding the current element
    """
    return [product(L[:index] + L[index + 1:]) for index, el in enumerate(L)]

def product(L: list) -> int:
    """
    Returns a product of all elements in a list
    """
    total = L[0]
    for el in L[1:]:
        total *= el
    return total

n = [1, 2, 3]
x = [i for i in range(1, 6)]
print(get_product_list(n), get_product_list(x), sep='\n')