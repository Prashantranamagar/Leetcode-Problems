"""
Source:https://leetcode.com/problems/longest-common-prefix/

Question:Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""

"""
Approach 1:
- Sort the given list of string.
- Store the start index string in first_string and last index string in last_string.
- store prefix on prifix = ""
- run loop while i < len(start_string) and i<len(last_string)
- check condition if start_index[i] != last_string[i] return prefix
- else increase prefix with prefix+=start_index[i]
- return prefix outside loop
"""


def longestCommonPrefix(strs):
    strs.sort()
    prefix=""
    first_string = strs[0]
    last_string = strs[-1]
    i=0
    while i<len(first_string) and i<len(last_string):
        if first_string[i] != last_string[i]:
            return prefix
        prefix += first_string[i]
        i+=1
    return prefix
        



"""
Approach:2
"""

# def longestCommonPrefix(strs):
    
#     if len(strs) == 0:
#         return ''
#     lcp = strs[0]
#     for item in strs:
#         for index in range(0, len(lcp)):
#             if index >= len(item) or lcp[index] != item[index]:
#                 lcp = lcp[0:index]
#                 break
            
#     return lcp
