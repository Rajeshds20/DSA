Given a array of N strings, find the longest common prefix among all strings present in the array.

You don't need to read input or print anything. Your task is to complete the function longestCommonPrefix() 
which takes the string array arr[] and its size N as inputs and returns the longest common prefix common in all the strings in the array. 
If there's no prefix common in all the strings, return "-1".




class Solution:
    def longestCommonPrefix(self, arr, n):
        # code here
        if (n==1):
            return arr[0]
        arr.sort()
        end = min(len(arr[0]), len(arr[n-1]))
        i = 0
        while(i<end and arr[0][i]==arr[n-1][i]):
            i += 1
        pre = arr[0][0:i]
        if pre=='':
            return '-1'
        return pre

