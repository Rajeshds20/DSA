'''
Given an array arr of n elements which is first increasing and then may be decreasing, find the maximum element in the array.
Note: If the array is increasing then just print then last element will be the maximum value.


You don't need to read input or print anything. 
Your task is to complete the function findMaximum() which takes the array arr[], 
and n as parameters and returns an integer denoting the answer.
'''


class Solution:
    def findMaximum(self, arr, n):
        # code here
        for i in range(n-1):
            if arr[i+1] < arr[i]:
                return arr[i]
        return arr[n-1]
