from Lib import re
#This daily coding problem resembles that of dcp113, but with a more delimiters that must also remain in that order
#So I think I can employ the same strategies that I used previously, but with more constraints

#Let's assume that anything not a letter/number is a delimiter

#First approach:
#We will split the string into subsections, including n words, and n-1 delimiters, then rejoin after
def rev_words_one(string:str):
    #First let's get the delimiters
    #Let's use regex to easily associate from alphanumerics
    # delimiters = list(filter(lambda x: x, re.split(r'[\w]+', string))) #Remove \b of start/end of string
    #Never mind, it's better to keep the extra delimiters!!!
    delimiters = re.split(r'\w+', string)
    # print(delimiters)
    #Next, let's split the words
    # words = re.findall(r'\w+', string)
    # print(words)
    #We could split multiple ways here.
    #Let's utilize the delimiters we already have found
    words = list(filter(lambda x: x, re.split(f'[{"".join(delimiters)}]', string))) #ie "[/:]" regex 
    words = list(reversed(words))
    #Now let's rejoin the lists, where if words is length n, delimiters is length n-1
    #So to zip it, we can add an arbitrary null char string
    return "".join([f'{de}{word}' for word, de in zip(words+[''], delimiters)])
    #I think this approach was pretty awesome, because I got to learn about regex
    #Feel strong about regex now, and also stronger about split/map/reduce/filter/etc...

#Now let's approach this from a similar way we did in dcp113
#We will not use any imported libraries first off
#So can we will assume that the string is mutable, aka a string list
def rev_words_two(string_list:list):
    #So...let's understand that the subsets of the list are defined by boundaries of incomparability
    #To make things simpler, let's assume that words are of lowercase characters
    #Let's iterate through the list once and build intervals of subsets
    swapflag = ('a' <= string_list[0] <= 'z') #Checks if it has gone from a word to a delimiter and vice versa
    i_start = 0
    words = []
    delimiters = []
    for i, c in enumerate(string_list+['']):
        if c == '':
            if swapflag: #Is tracking word
                words.append("".join(string_list[i_start:i]))
            else:
                delimiters.append("".join(string_list[i_start:i]))
            continue
        if 'a' <= c <= 'z':
            if swapflag:
                continue
            else:
                delimiters.append("".join(string_list[i_start:i]))
                swapflag=True
                i_start=i
                continue
        #Otherwise check that c is a delimiter basically, as long as it's not '', which is null terminator for us
        if swapflag:
            swapflag = False
            words.append("".join(string_list[i_start:i]))
            i_start = i
            continue
        else:
            continue
    # print(words, delimiters)
    words = list(reversed(words))
    #Now let's combine those lists
    swapflag = ('a' <= string_list[0] <= 'z') #Check if string begins with \w or \W
    #Longer one goes first, else if same length, swapflag decides who goes first
    lst1, lst2 = (words, delimiters) if len(words) >= len(delimiters) and swapflag else (delimiters, words)
    if len(lst1) != len(lst2):
        lst2.append('')
    reversed_string = ''.join([f'{one}{two}' for one, two in zip(lst1, lst2)])
    return reversed_string
    #This is done!
    #A lot less clean, but it does it...
    #not in place. Is that efficiently possible?

if __name__ == "__main__":
    string1 = "hello/world:here"
    string2 = "hello/world:here/"
    string3 = "hello//world:here"
    string4 = r"\\/|hello//world:here!!*"
    #Note: "\word|word*" will cause problems for the regex, ONLY r'\\word|word*' has shown to work. Why?
    # rev_str = rev_words_one(string3)
    print(rev_words_one(string1))
    print(rev_words_one(string2))
    print(rev_words_one(string3))
    print(rev_words_one(string4))
    print(rev_words_two(list(string1)))
    print(rev_words_two(list(string2)))
    print(rev_words_two(list(string3)))
    print(rev_words_two(list(string4)))