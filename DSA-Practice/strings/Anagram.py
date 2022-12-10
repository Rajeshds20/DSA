'''
Given two strings a and b consisting of lowercase characters.
The task is to check whether two given strings are an anagram of each other or not.
An anagram of a string is another string that contains the same characters, only the order of characters can be different.
For example, act and tac are an anagram of each other.
'''


from collections import Counter

class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,string1,string2):
        #code here
        a = Counter(string1)
        b = Counter(string2)
        return True if a==b else False
