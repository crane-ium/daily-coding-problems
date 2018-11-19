#Given two strings, identify if one is shifted transformation of the other

def is_shifted_one(s1:str, s2:str):
    #Let's start with a basic shift check
    #This will be a more brute force emthod
    if(len(s1) != len(s2)):
        return False
    lst = []
    for i, c1 in enumerate(s1):
        if(c1 == s2[0]):
            lst.append(i)
    #Time for these loops is O(kn); k: occurences of s2[0], n: len of s1
    for start in lst: #Run a bool test on each element in lst
        flag = True
        for i in range(1, len(s1)):
            if(s1[(start + i) % len(s1)] != s2[i]):
                flag = False
                break
        if(flag):
            return True
    #Worst case: The entire string is the one letter but one, and that difference is at the end
    #eg. 'aaab' vs 'abaa' which will be n^2 time
    return False #Hit end, no match found

if __name__ == "__main__":
    s1 = 'abc'
    s2 = 'bac'
    print(f'Shifted? {"Yes" if is_shifted_one(s1, s2) else "No"}')