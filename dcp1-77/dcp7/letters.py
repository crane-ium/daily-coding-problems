"""
Prompt:
Facebook

Given the mapping a=1, b=2, ...z=26 and an encoded msg, count the number of ways it can be decoded

For example,
'111' would give 3, since it could be 'aaa', 'ka', and 'ak'

You can assume messages are decodable. '001' is not allowed
"""

from collections import deque
from collections import defaultdict

def map_letters():
    """
    Returns a list of letters mapped to an index
    """
    letters = [None]
    for i in range(27):
        letters.append(chr(97 + i))
    return letters

def deserialize(input: str):
    """
    Returns a list of all possible strings
    """
    str_list = [input]
    str_des = [''] #Maps to the string_list
    str_letters = map_letters()
    all_empty = False
    while not all_empty:
        all_empty = True #If this is true at the end, exit
        for index, string in enumerate(str_list):
            # if string == '': #Wait, i can't do this...
            #     del str_list[index]
            #     del str_des[index]
            #     continue
            if string != '':
                all_empty = False
            else:
                continue
            if string[0] == '0':
                del str_list[index]
                del str_des[index]
                continue
            if string[0] == '1':
                if len(string) > 1:
                    str_list.append(string[2:])
                    str_des.append(str_des[index] + str_letters[int(string[0:2])])
                str_des[index] = str_des[index] + str_letters[int(string[0])]
                str_list[index] = string[1:]
            elif string[0] == '2' and len(string) > 1 and string[1] <= '6':
                str_list.append(string[2:])
                str_des.append(str_des[index] + str_letters[int(string[0:2])])
                str_des[index] = str_des[index] + str_letters[int(string[0])]
                str_list[index] = string[1:]
            else:
                str_des[index] = str_des[index] + str_letters[int(string[0])]
                str_list[index] = string[1:]
        # print(str_des)
    return str_des, len(str_list)

def deserialize_count(input: str):
    """
    Return the number of deserialize combinations the input can return
    """
    string_list = [input]
    count = 0
    while string_list:
        for index, string in enumerate(string_list):
            if string == '':
                del string_list[index]
                count += 1
                continue
            if string[0] == '0': #Not allowed
                del string_list[index]
                continue
            if string[0] == '1':
                if len(string) > 1:
                    string_list.append(string[2:]) 
                string_list[index] = string[1:]
            elif string[0] == '2' and len(string) > 1 and string[1] <= '6':
                string_list.append(string[2:])
                string_list[index] = string[1:]
            else:
                string_list[index] = string[1:]
    return count

#This is the algorithm that was in the solution
def num_encoding(s: str):
    """
    Return the count of possible deserializations of the string
    """
    cache = defaultdict(int)
    cache[len(s)] = 1
    
    for i in reversed(range(len(s))):
        if s[i].startswith('0'):
            cache[i] = 0
        elif i == len(s):
            cache[i] = 1
        else:
            if int(s[i:i + 2]) <= 26:
                cache[i] = cache[i + 2]
            cache[i] += cache[i + 1]
    return cache[0]

if __name__ == "__main__":
    input = '11111243'
    # print(deserialize_count(input))
    strings, count = deserialize(input) #Not good time or space complexity
    print(f'Strings: {strings}\nCombinations: {count}')
    count = num_encoding(input)
    print(f'Combinations: {count}')