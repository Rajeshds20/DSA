'''
Given an integer array and another integer element. The task is to find if the given element is present in array or not.
if Present, return Index, else return -1.

The task is to complete the function search() which takes the array arr[], 
its size N and the element X as inputs and returns the index of first occurrence of X in the given array. 
If the element X does not exist in the array, the function should return -1.
'''


class Solution:
    # Complete the below function
    def search(self, arr, N, X):
        # Your code here
        for i in range(N):
            if arr[i] == X:
                return i
        return -1
