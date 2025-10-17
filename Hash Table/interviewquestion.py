"""
given two list find the common item from both list
Approach:
1. Naive way using nested loop
2. Optimize solution using hash table(i.e. builtin dictionary in python)
"""
list1 = [2, 9, 20]
list2 = [5, 2, 10]

#Naive way O(n)
def common_item(list1, list2):
    items = []
    for i in list1:
        for j in list2:
            if i == j:
                items.append(i)
    return items
print("#################### Naive solution #################")                
print(common_item(list1, list2))


#Optimize Solution using hash table(dictionary)\

def common_item_optimized(list1, list2):
    hash = {}
    for item in list1:
        hash[item] = True
    result = []
    for item in list2:
        if item in hash:
            result.append(item)
    return result
print("#################### Optimized solution #################")                

print(common_item_optimized(list1, list2))