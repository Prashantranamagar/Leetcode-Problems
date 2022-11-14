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