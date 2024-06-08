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

Approaches:
1.Mapping
--> Make charmap for both inputs and check the if the char count in charmap are equal
2.Sorting 
-->Sort the given string and check if they are equal


"""

# Solution 1  Time complexity : O(n)

def counter_map(string):
    char_map = {}
    for char in string:
        if char in char_map:
            char_map[char] += 1
        else:
            char_map[char] = 0
    return char_map


def isAnagram(s, t):
    charmap = counter_map(s)
    charmap1 = counter_map(t)
    print (charmap, charmap1)
    # for char in charmap:
    if charmap == charmap1:
        print('True') 
        return True

    print('false')
    return False

s = "anagram"
t = "nagaram"

isAnagram(s,t)


# Solution 2 using Counter from collections. it is just like the counter_map function we make in sol 1. Time complexity: O(n)

from collections import Counter
def isAnagram(s, t):
    charmap = Counter(s)
    charmap1 = Counter(t)
    print (charmap, charmap1)
    # for char in charmap:
    if charmap == charmap1:
        print('True') 
        return True

    print('false')
    return False

