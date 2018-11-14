#Find the sequence of contiguous numbers that sum up N

def sequence_sum(N, sequence):
    """
    Returns a list of sequences that can be summed to equal N
    -Does not work on sequences containing negative numbers
    """
    #Search through the list using two search pointers
    left, right = 0, 0
    sequence_list = [] #All the contiguous sequences in the given sequence that sum to N
    #Avoid nested loops
    total = sequence[0]
    while(left < len(sequence)):
        if total > N:
            if left < right:
                left += 1
                if left > 0:
                    total -= sequence[left-1]
            else:
                left += 1
                right += 1
                total = sequence[left]
        elif total < N:
            right += 1
            if right == len(sequence):
                break
            total += sequence[right]
        else: #total == N
            sequence_list.append(sequence[left:right+1])
            left += 1
            right += 1
            if right == len(sequence):
                break
            total -= sequence[left-1]
            total += sequence[right]
    return sequence_list

def seq_sum(N: int, seq: list):
    """
    Return a list of sequences that sum into N
    -Should support negative numbers
    -This uses the memoization algorithm similar to the given solution
     -Modified to return a list of possible sequences rather than just one
    """
    sum_dict = dict()
    sum = 0
    sum_dict[0] = [-1] #Set the base index where sum is 0
    seq_list = []
    for i, val in enumerate(seq):
        sum += val
        if sum not in sum_dict:
            sum_dict[sum] = []
        sum_dict[sum].append(i)
        first_i = sum_dict.get(sum - N) #Search for a stored data where delta sum = (N)
        if first_i is not None:
            for ii in first_i:
                seq_list.append(seq[ii+1:i+1])
    return seq_list
        

if __name__ == "__main__":
    seq = [-2, 7 , 5, -1, 4, -2, -3, 1]
    seq2 = [1, -2, 7, 3, 5]
    seq3 = [-2, 7, 3, 5, -4, -1]
    lsts = seq_sum(9, seq)
    print("Lists: ", lsts)
    print("Lists2: ", seq_sum(8, seq2))
    print("Lists3: ", seq_sum(8, seq3))