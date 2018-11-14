from collections import defaultdict
"""
dcp103
Shortest substring containing a set of characters
-Returns the shortest ordered substring for an unordered set
"""

def get_substring(string: str, items: set)->str:
    #Have map that tracks the shortest
    # set_chars = defaultdict([]) #Tracks the last occurence of a character

    if len(items) == 0:
        return ""
    set_copy = items.copy()
    shortest = len(string)
    interval = (0, len(string))
    #Let's brute force it here...
    for i, c in enumerate(string):
        if c not in items:
            continue
        set_copy = items.copy()
        set_copy.remove(c)
        print(set_copy, string[i+1:])
        count = int()
        for count, cc in enumerate(string[i+1:]):
            if cc in set_copy:
                set_copy.remove(cc)
            if count >= shortest or not set_copy:
                break
        if count + 2 < shortest and not set_copy:
            shortest = count+2
            interval = (i, i+count+2)
    return string[interval[0]:interval[1]]
    # for i, c in enumerate(str):
    #     if c in items:
    #         set_chars[c].append(i)
    # for c in items:
    # char_i = defaultdict([])
    # for i, c in enumerate(string):
    #     if c in items:
    #         char_i[i].append(c)
    
                

if __name__ == "__main__":
    string = "figehaeci"
    print("Shortest substr:",get_substring(string, set({'a', 'e', 'i'})))