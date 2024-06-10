"""
Add Binary

Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
 
"""


# Solution 1
    
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        first find the lenght of both the string
        make length of both string eual by adding 0 ahead of the string
        initialize carry  = 0 and result = '' i = mex_length-1  
        loop through the max_length
        calculate sum = carry + int(a[index]) + (b[index])
        result = str(sum % 2) + result
        carry = sum // 2 
        after loop is completed 
        check for value of carry if carry is 0 then return res if carry is 1 
        return by adding 1 infront of the res
        """
        len_a = len(a)
        len_b = len(b)
        max_len = max(len_a, len_b)- 1

        if len_a > len_b:
            diff = len_a - len_b
            b ='0'*diff + b  
        else:
             diff = len_b-len_a
             a = '0'*diff + a
        res = ''
        carry = 0
        for i in range(max_len, -1, -1):
            sum = carry + int(a[i]) + int(b[i])
            res = str(sum % 2) + res
            carry = sum // 2

        if carry == 1:
            res = str(carry) + res
        
        return res


        

#Solution 2
from itertools import zip_longest
class Solution:
  def addBinary(self, a: str, b: str) -> str:
    carry = 0
    result = []

    # Use zip_longest to iterate over the strings in reverse, filling with '0'
    for x, y in zip_longest(reversed(a), reversed(b), fillvalue='0'):
      total = carry + int(x) + int(y)
      result.append(str(total % 2))  # current binary digit
      carry = total // 2  # new carry

    # If there's a carry left, append it
    if carry:
      result.append('1')

    # Join the result and reverse it to get the final binary string
    return ''.join(reversed(result))