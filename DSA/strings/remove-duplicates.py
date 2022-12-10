Given a string without spaces, the task is to remove duplicates from it.

Note: The original order of characters must be kept the same. 

Your task is to complete the function removeDups() which takes a single string 
as input and returns the string. You need not take any input or print anything.



class Solution:
	def removeDups(self, S):
		# code here
		d = ''
		for i in s:
		    if i not in d:
		        d+=i
		return d


