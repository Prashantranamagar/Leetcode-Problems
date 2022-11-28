"""
Source:https://www.geeksforgeeks.org/print-all-the-duplicates-in-the-input-string/
"""

def printallduplicates(string):
    map ={}
    for i in range(len(string)):
        if string[i] in map:
            map[string[i]] += 1
        else:
            map[string[i]] = 1
    
    for item in map:
        if map[item] > 1:
            print(item)


printallduplicates('abcdefa')