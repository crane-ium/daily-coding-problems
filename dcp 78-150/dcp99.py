from collections import defaultdict
from random import randint
def consecutive_sequence(arr: list):
    int_dict = defaultdict(lambda: 0)
    for i in arr:
        int_dict[i] = 1
    current_max = 1
    total_max = 1
    for i in arr:
        if(int_dict[i]==0):
            continue #Prevent it from doing anything more if it's alerady been checked
        a = 1
        int_dict[i] = 0
        while(int_dict[i+a]!=0):
            current_max += 1
            int_dict[i+a] = 0
            a += 1
        a = 1
        while(int_dict[i-a]!=0):
            current_max += 1
            int_dict[i-a] = 0
            a += 1
        if current_max > total_max:
            total_max = current_max
        current_max = 1
    return total_max
def given_solution(nums: list):
    max_len = 0
    int_dict = dict()
    for num in nums:
        if num in int_dict: #skip dupes
            continue
        left_bound, right_bound = num, num
        if num -1 in int_dict:
            left_bound = int_dict[num - 1][0]
        if num + 1 in int_dict:
            right_bound = int_dict[num + 1][1]
        int_dict[num] = (left_bound, right_bound)
        int_dict[left_bound] = (left_bound, right_bound)
        int_dict[right_bound] = (left_bound, right_bound)
        max_len = (right_bound - left_bound + 1) if max_len < (right_bound - left_bound + 1) else max_len
    return max_len

if __name__ == "__main__":
    lst = [randint(0, 6) for i in range(10)]
    consecutive_count = consecutive_sequence(lst)
    cons_count2 = given_solution(lst)
    lst.sort()
    print(f'List: {lst}\nConsecutive Integers: {consecutive_count}\nGiven Solution: {cons_count2}')
    lst = [200, 4, 100, 3, 1, 2]
    consecutive_count = consecutive_sequence(lst)
    cons_count2 = given_solution(lst)
    lst.sort()
    print(f'List: {lst}\nConsecutive Integers: {consecutive_count}\nGiven Solution: {cons_count2}')