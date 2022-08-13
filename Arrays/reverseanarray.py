"""
Reverse given array
Source: https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/

"""

def reverse(arr):
    reversed = []
    i=len(arr)-1
    while i>=0:
        reversed.append(arr[i])
        i-=1
    return reversed