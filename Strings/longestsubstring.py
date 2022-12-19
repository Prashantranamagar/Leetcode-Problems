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

# s = "abcabcbb"

#Brute Force
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



#Optimal
s = "abcabcbb"
def lengthOfLongestSubstring(s):
    se = set()
    left = 0
    count =0
    for right in range(len(s)):
        if s[right] in se:
            se.remove(s[left])
            left+=1
        se.add(s[right])
        count = max(count, right-left+1)
    return count




print(lengthOfLongestSubstring(s))


