"""
Source:https://leetcode.com/problems/valid-palindrome/

Question: Valid palindrome

Examples:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

"""


def palindrome(str):
    outstr = ''
    for char in str:
        if char.isalnum():
            outstr += char
    if outstr.lower() == outstr.lower()[::-1]:
        return True
    return False





# #Expand from the center
# import math 
# def palindrome(str):
#     # for odd length
#     mid = math.floor(len(str)/2)
#     left, right = mid, mid

#     while right<len(str) and left>=0 and str[left]==str[right]:
#         left -= 1
#         right +=1
#         return True

#     #for even length
#     mid = math.floor(len(str)/2)
#     left, right = mid, mid+1

#     while right<len(str) and left>=0 and str[left]==str[right]:
#         left -= 1
#         right +=1
#         return True




