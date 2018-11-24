
#Reverse words in a string, seperated by a space
#We can do a straightforward approach using builtins
def reverse_words(s:str)->str:
    rev = str()
    rev += ' '.join(reversed(s.split(' '))) #Pretty simple way to reverse it, but not-inplace
    return rev

def reverse_inplace(s:list)->list:
    #So, maybe the best way to do this is to...
    #Take that string and let's reverse it in-place
    #We must assume the string is mutable, and in this case we can just use a list to represent the string
    for i in range(0, len(s)//2):
        s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]
    #Now in-place reverse each word
    i_start, i_end = 0, 0
    for i, c in enumerate(s+[' ']):
        if c == ' ':
            i_end = i
            for x in range(0, (i_end-i_start+1)//2): #iterate through half a word
                  s[i_start+x], s[i_end-1-x] = s[i_end-1-x], s[i_start+x]
            i_start = i+1
    return s

if __name__ == "__main__":
    s = "hello world here"
    slist = list(s)
    print(reverse_words(s))
    print(s)
    print(reverse_inplace(slist))
    print(''.join(slist))