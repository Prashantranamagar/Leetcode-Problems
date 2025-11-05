"""
Min and max in an array:

Approaches:
Approach 1: Native Approach Time complexity O(n), Space Complexity O(1)

min = first arr item
max = first arr item
run loop in arry 
compare min wih each element and if arry item less than min  update value
same of max

Approach 2: Using Sorting Algorithm -->did  not work O(nlogn)

"""

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]


# Approach 1 : Native Approach

def find_min_max(arr):
    min = arr[0]
    max = arr[0]
    for item in arr:
        if item < min:
            min = item
        if item > max:
            max = item
    return min, max

print(find_min_max(arr))