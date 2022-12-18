"""
Longest Substring Without Repeating Characters

Source:https://leetcode.com/problems/longest-substring-without-repeating-characters/

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

a b c a b c b b
  i j
"""

s = "abcabcbb"


# def lengthOfLongestSubstring(s):
#     maxcount = 0
#     if len(s) == 1:
#             return 1
#     for i in range(len(s)-1):
#         count=1
#         for j in range(i+1, len(s)):
#             if s[j] not in s[i:j]:
#                 print(s[i], s[j])
#                 count = count +1 
#             else:
#                 break
            
#         maxcount = max(maxcount, count)   
#     return maxcount




def lengthOfLongestSubstring(s):
    start = maxLength = 0
    usedChar = {}
    
    for i in range(len(s)):
        if s[i] in usedChar and start <= usedChar[s[i]]:
            start = usedChar[s[i]] + 1
        else:
            maxLength = max(maxLength, i - start + 1)

        usedChar[s[i]] = i

    return maxLength


print(lengthOfLongestSubstring(s))


