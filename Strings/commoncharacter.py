"""

Find Common Characters

Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). 
You may return the answer in any order.

"""



"""


Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]

"""


# Solution 1:

class Solution(object):

    def charmap(self, char):
        map = {}
        length = len(char)
        for i in range(0, length):
            if char[i] not in map:
                map[char[i]] = 1
            else:
                map[char[i]] += 1
        return map

    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        first_char = words[0]
        map = self.charmap(first_char)
        words_len = len(words)   

        for i in range (1, words_len):
            map2 = self.charmap(words[i])
            print(map2)
            for i in map.keys():
                if i in map2.keys():
                    if map[i] <= map2[i]:
                        map[i] = map[i]
                    else:
                        map[i] = map2[i]
                else:
                    map[i] = 0

        result = []

        for i in map.keys():
            print(i)
            if map[i] > 0:
                for j in range(0, map[i]):
                    result.append(i)
                
        return result




# Example 2:
from collections import Counter
from functools import reduce
from operator import and_

class Solution(object):
    def commonChars(self, words):
        return reduce(and_, map(Counter, words)).elements()
    

"""
map(Counter, words)
This part converts each word in the words list into a Counter object. 
A Counter is a dictionary subclass that counts the occurrences of each character in the word. For 
Eg:
words = ["bella", "label", "roller"]
Counters = map(Counter, words)
output:
[Counter({'b': 1, 'e': 1, 'l': 2, 'a': 1}),
 Counter({'l': 2, 'a': 1, 'b': 1, 'e': 1}),
 Counter({'r': 2, 'o': 1, 'l': 2, 'e': 1})]

 
 reduce(and_, map(Counter, words))
 The reduce function applies the and_ operator (which computes the intersection) across all Counter objects. 
 This intersection operation keeps only the elements (characters) that are present in all Counters with their minimum counts

 
 common_counts.elements()
 The elements() method of a Counter object returns an iterator over elements repeating each as many times as its count. If common_counts is Counter({'l': 2, 'e': 1})

"""