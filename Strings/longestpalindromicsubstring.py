"""
Source:https://leetcode.com/problems/longest-palindromic-substring/description/

Question:Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Approach:
1.BruteForce.
1.Expand from the center to check palindromic substring.
"""

# 1.Expand from the center to check palindromic substring.

def longestPalindrome(self, s):
    #Approach:Expand from the center.
    result = ''
    result_len =0

    for i in range(len(s)):   

        #for odd length
        left, right=i, i
        while right<len(s) and left>=0 and s[left]==s[right]:  #check for pallendrome
            if (right-left+1) > result_len: #check if len of substring is greater than result_len
                result = s[left:right+1] #update result
                result_len = right-left+1 #update result len
        left -= 1
        right += 1

        #for even length
        left, right = i, i+1
        while right<len(s) and left>=0 and s[left]==s[right]:  #check for pallendrome
            if (right-left+1) > result_len:
                result = s[left:right+1] 
                result_len = right-left+1
        left -= 1
        right += 1
        
    return result

            