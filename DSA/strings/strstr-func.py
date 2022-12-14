'''
Your task is to implement the function strstr. The function takes two strings as arguments (s,x) and 
locates the occurrence of the string x in the string s. 
The function returns and integer denoting the first occurrence of the string x in s (0 based indexing).

You don't have to take any input. Just complete the strstr() function which takes two strings str, target as an input parameter. 
The function returns -1 if no match if found else it returns an integer denoting the first occurrence of the x in the string s.
'''


def strstr(s, x):
    # code here
    n = len(s)
    m = len(x)
    for i in range(n-m+1):
        if s[i:i+m] == x:
            return i
    return -1
