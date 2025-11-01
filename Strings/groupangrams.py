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

Two Approaches: Both using HashMap
1. Sort each string and use the sorted string as key in hashmap. Time complexity O(n · k log k)  k = length of string, n = no of string
2. Use count of each character as key in hashmap. Time complexity O(n · k)  k = length of string, n = no of string

"""

######################################################################
#Approach 1: Using sorted string as key in hashmap  wihout defaultdict
#################################################`#####################
strs = ["eat","tea","tan","ate","nat","bat"]

#Time complexity O(n · k log k)  k = length of string, n = no of string
# def groupAnagrams(strs):
#     map = {}
#     for item in strs:
#         key = ''.join(sorted(item)) # sorted function always return a list so converted it to string using join
#         print(key)
#         if key not in map:
#             map[key] = []
#         map[key].append(item)
#     groupAnagrams = []
#     for item in map.values():
#         groupAnagrams.append(item)
#     return groupAnagrams
            
# print(groupAnagrams(strs))




######################################################################
#Approach 1: Using sorted string as key in hashmap  with
#   defaultdict
#################################################`#####################
"""
Step-by-step execution with states

Initialization

dic = defaultdict(list)
dic is an empty defaultdict whose default value for missing keys is [].
State: dic = {}
First loop iteration: item = "eat"
key = ''.join(sorted("eat"))   # sorted("eat") -> ['a','e','t']
key = "aet"
dic[key].append("eat")
Key computed: "aet"
dic["aet"] becomes ["eat"] (default list created and eat appended).
State: dic = {"aet": ["eat"]}
Second iteration: item = "tea"
key = ''.join(sorted("tea"))  # -> "aet"
dic["aet"].append("tea")
Key: "aet" (same as for "eat")
Append "tea" into the existing list under "aet".
State: dic = {"aet": ["eat", "tea"]}
Third iteration: item = "tan"
key = ''.join(sorted("tan"))  # sorted -> ['a','n','t'] -> "ant"
dic["ant"].append("tan")
Key: "ant"
New list created for "ant" and "tan" appended.
State: dic = {"aet": ["eat", "tea"], "ant": ["tan"]}
Fourth iteration: item = "ate"
key = ''.join(sorted("ate"))  # -> "aet"
dic["aet"].append("ate")
Key: "aet"
Append "ate" to the "aet" bucket.
State: dic = {"aet": ["eat", "tea", "ate"], "ant": ["tan"]}
Fifth iteration: item = "nat"
key = ''.join(sorted("nat"))  # -> "ant"
dic["ant"].append("nat")
Key: "ant"
Append "nat" to the "ant" bucket.
State: dic = {"aet": ["eat", "tea", "ate"], "ant": ["tan", "nat"]}
Sixth iteration: item = "bat"
key = ''.join(sorted("bat"))  # -> "abt"
dic["abt"].append("bat")
Key: "abt"
New bucket "abt" created and "bat" appended.
State after loop end:
dic = {"aet": ["eat", "tea", "ate"], "ant": ["tan", "nat"], "abt": ["bat"]}
Building the result list
result = []
for i in dic:
    result.append(dic[i])
Iteration order of keys in dic is insertion order (Python 3.7+), so keys come out as "aet", "ant", "abt".
Append dic["aet"] → result = [["eat", "tea", "ate"]]
Append dic["ant"] → result = [["eat", "tea", "ate"], ["tan", "nat"]]
Append dic["abt"] → result = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
Final return value
[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
(Any ordering of the groups is acceptable; within each group the words are in the order they were encountered.)

"""


# Same as above just using default dict to determine the type of value store in dict.
from collections import defaultdict

# def groupAnagrams(strs):
#     """
#     :type strs: List[str]
#     :rtype: List[List[str]]
#     """
#     dic = defaultdict(list)
#     for item in strs:
#         key = ''.join(sorted(item))
#         dic[key].append(item)
#     result = []
#     for i in dic:
#         result.append(dic[i])
#     return result







######################################################################
#Approach 2: Using count of characters as key in hashmap    Time Complexity O(n · k)  k = length of string, n = no of string
#################################################`#####################


def group_anagram(strs):
    """ 
    1. Create empty map
    2. Iterate through the list.
    3. set a freq counter that count the freq of each aphabet form a-z  with 26 zeros 
    4. loop over the word
    5. check the position of the alphabet in the fequency counter with  ord(char)- ord(a) --> ord gives the ascci value of the alphabet.
    6. increment the position with 1
    7. after finishing the first loop in the word set the freq counter to key in the dict and append the word in value as list.
    8 .if same key the the value will appen in the same key if not it craete new key with value as list
    9. afte the map is complete
    10.append all the value in a list and return it. 

    """

    map = {}
    for item in strs:
        freq = [0]*26
        for char in item:
            freq[ord(char) - ord('a')] += 1
        key = tuple(freq)
        if not key in map:
            map[key] = []
        map[key].append(item)
    print(map)

    group_anagram = []
    for item in map:
        group_anagram.append(map[item])
    
    # # or
    # group_anagram = list(map.values())
    
    return group_anagram
    

print(group_anagram(strs))
