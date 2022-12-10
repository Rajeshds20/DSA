'''
Given an integer array coins[ ] of size N representing different denominations of currency and an integer sum, find the number of ways you can make sum by using different combinations from coins[ ].  
Note: Assume that you have an infinite supply of each type of coin. 


You don't need to read input or print anything. Your task is to complete the function count() which accepts an array coins[ ] 
its size N and sum as input parameters and returns the number of ways to make change for given sum of money. 
'''


class Solution:
    def count(self, coins, N, sum):
        # code here
        n = N
        table = [[0 for x in range(n)] for x in range(sum+1)]
        for i in range(n):
            table[0][i] = 1
        for i in range(1, sum+1):
            for j in range(n):
                x = table[i - coins[j]][j] if i-coins[j] >= 0 else 0
                y = table[i][j-1] if j >= 1 else 0
                table[i][j] = x + y
        return table[sum][n-1]
