#Find all anagrams of string in another string

#First let's design a simple brute force method
def anagram_finder(s1, s2):
    indeces = []
    for i, c in enumerate(s2):
        #Search each c in s2
        if s1 == s2[i:i+len(s1)]:
            indeces.append(i)
        if s1[-1::-1] == s2[i:i+len(s1)]:
            indeces.append(i)
    return indeces

if __name__ == "__main__":
    words = ['ab', 'abcd']
    strings = ['abxaba', 'abcdcba']
    for w, s in zip(words, strings):
        print(f'Slow Indeces: {anagram_finder(w, s)}')