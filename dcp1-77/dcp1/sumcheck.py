"""
Prompt:
This problem was recently asked by Google
Given a list of numbers and a number k, return whether any two numbers from the list add up to k
For example, given [10, 15, 3, 7] and k = 17, return true since 10 + 7 == 17
"""

class SumCheck(object):

    def is_sum1(self, k: int, L:list) -> bool:
        """
        Return true whether there a list contains two numbers that sum to k
        """
        for index, n in enumerate(L):
            for i in L[index+1:]:
                if i + n == k:
                    return True
        return False

if __name__ == "__main__":
    L1 = [10, 15, 3, 7]
    L2 = [1, 2, 3, 4]
    L3 = [n for n in range(2, 21, 2)]
    s = SumCheck()
    print(s.is_sum1(17, L1), #True
          s.is_sum1(8, L2),  #False
          s.is_sum1(20, L3), #True
          s.is_sum1(3, L3),  #False
          s.is_sum1(4, L3),  #False
          s.is_sum1(6, L3)   #True
    )
