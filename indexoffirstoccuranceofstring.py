""""
Find the Index of the First Occurrence in a String
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

"""


# Solution 1

class Solution:
    def strStr(self, haystack, needle):
        length_haystack = len(haystack)
        length_needle = len(needle)
        # Edge Cases if neddle is longer than haystack
        if length_needle > length_haystack:
            return -1

        if length_needle == 0:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1


# Solution 2 just to use the buildin string find method

haystack, needle = "butsadbutsad", "sad"
print(haystack.find(needle))  # find the first occurance of needle in haystack
# Output: 3
print(haystack.count(needle))  # find how may times the neddle is present in haystack
# Output: 2
