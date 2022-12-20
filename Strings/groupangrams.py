"""
Source:https://leetcode.com/problems/group-anagrams/description/

Questions:Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using 
all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]


"""


from collections import defaultdict


def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    dic = defaultdict(list)
    for item in strs:
        key = ''.join(sorted(item))
        dic[key].append(item)
    result = []
    for i in dic:
        result.append(dic[i])
    return result