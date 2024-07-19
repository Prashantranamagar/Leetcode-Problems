"""

Source:https://leetcode.com/problems/search-in-rotated-sorted-array/

Examples:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Input: nums = [1], target = 0
Output: -1

"""

"""
Approach 1 (Normal Approach): Brute force using loop if item = target return the index. Time Complexity: O(n)

Approach 2 (Optimized Approach): Using Binary Serach
            1. initialize left and right pointer at first and last index.
            2. while left <= right:
            3.  find mid = left + right // 2
                 if my_list(mid) == target return mid
            4.  find the sorted half is it it the left half or right half.
                if sorted half is in left i.e my_list[left] <= my_list[mid]
                    find if the target is in the sorted half i.e
                    if my_list[low] =< target and target =< mylist[high]: 
                        eliminate the right half right = mid-1
                    if not
                    else:
                        eliminate the left half ie. target is in right half  left = mid + 1
                if not
                else: right half is sorted.
                    if target is in  sorted half ie. right half
                    if my_list[high] >= target and target >= my_list[mid]:
                        eliminate left half left = mid + 1
                    if not
                    else:
                        eliminate right half right  = mid - 1                      
"""


my_list = [4,5,6,7,0,1,2]
target = 5

################################################################
# TIPS USE BINARY SEARCH FIND SORTED HALF LEFT OR RIGHT
# CHECK IF THE TARGET IS IS IN SORTED HALF OR UNSORTED HALF FOR BOTH CONDITION
# i.e when left half sorted or when right half is sorted
###############################################################

# Tips find whether the sorted half is left or right  
    #if left find where the target is if it is in left sorted half
        # right = right -1
    #else 
        #left = left +1
    #if right half is sorted find the target if in right sorted half
        # left = left + 1
    #else:
        #right = right -1


def search_in_rotated_sorted_array(my_list):
    left = 0
    right = len(my_list) -1

    while left <= right:
        mid = (left + right) // 2
        if target == my_list[mid]:
            return mid
        if my_list[left] <= my_list[mid]:  # left half is sorted.
            if my_list[left] <= target and target <= my_list[mid]:  # target is in left sorted half
                right = mid - 1
            else:  # target is in right unsorted half
                left = mid + 1
        else:  # Right half is sorted
            if my_list[right] >= target and target >= my_list[mid]:  # target is in right sorted half
                left = mid + 1
            else:  # target is in left unsorted half
                right = mid - 1
    return -1



print(search_in_rotated_sorted_array(my_list))
