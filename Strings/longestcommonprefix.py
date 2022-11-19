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



def longestCommonPrefix(strs):
    
    if len(strs) == 0:
        return ''
    lcp = strs[0]
    for item in strs:
        for index in range(0, len(lcp)):
            if index >= len(item) or lcp[index] != item[index]:
                lcp = lcp[0:index]
                break
            
    return lcp