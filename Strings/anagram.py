"""
Source:https://leetcode.com/problems/valid-anagram/submissions/

Question:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Examples:
Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false

"""


def isAnagram(s, t):
    charmap = {}
    for char in s:
        if char in charmap:
            charmap[char] += 1
        else:
            charmap[char] = 0

    charmap1 = {}
    for char in t:
        if char in charmap1:
            charmap1[char] += 1
        else:
            charmap1[char] = 0

    for char in charmap:
        if charmap == charmap1:
            return True
        return False
