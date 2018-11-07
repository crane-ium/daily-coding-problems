def give_int_list(i_str):
    #Turns it into an list of integers from a string
    stoi = [ord(c)-48 for c in i_str]
    return stoi
def give_full_int(i_list):
    total = 0
    for i, n in enumerate(i_list):
        total += 10**(len(i_list)-i - 1) * n
    return total
def move_up(i_list, old_index, new_index):
    for i in range(old_index, new_index, -1):
        i_list[i-1] ^= i_list[i]
        i_list[i] ^= i_list[i-1]
        i_list[i-1] ^= i_list[i]
def sort_end_range(i_list, index):
    #Sorts the elements of index onward
    for i in range(index, len(i_list)):
        for n in range(index, i):
            if i_list[i] < i_list[n]:
                move_up(i_list, i, index)

def get_indeces(i_list):
    for i in range(len(i_list)-1, 0, -1):
        for n in range(i-1, -1, -1):
            # print(f'{i_list[i]} vs {i_list[n]}')
            if i_list[i] > i_list[n]:
                return (i, n)
    return(0, -1)
def next_lex_permutation(i_list):
    #Nested loops to find...
    #First: Index to increase, and which index to move up into it
    i, j = get_indeces(i_list)
    if(i == 0 or j==-1):
        sort_end_range(i_list,0)
    else:
        move_up(i_list, i, j)
        sort_end_range(i_list, i)

int_list = give_int_list("4321")
base_list = int_list.copy()
next_lex_permutation(int_list)
print(int_list)
while(int_list != base_list):
    next_lex_permutation(int_list)
    print(int_list)
# move_up(int_list, 2, 0)
# number = give_full_int(int_list)
# print(number)
# i = 5
# j = 33
# i ^= j
# j ^= i
# i ^= j
# print(i, j)