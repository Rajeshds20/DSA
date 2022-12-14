'''
Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.


You don't need to read input or print anything. Complete the function MissingNumber() 
that takes array and N as input  parameters and returns the value of the missing number.
'''


class Solution:
    def MissingNumber(self, array, n):
        # code here
        array.sort()
        a = set(range(1, n+1))
        b = a-set(array)
        return list(b)[0]
