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
            1. initialize lefit and right pointer at first and last half.
            2. while left <= right:
            3. fing mid = left + right // 2
            2. find the sorted half is it it the left half or right half.

                3. if left is sorted then
                4. check if the target is in the sorted half or not 
                5. if  yes my_list[low] =< target and target =< mylist[high]: then 
                    eliminate the right half right = mid-1
                else:
                    eliminate the left half ie. target is in right half  left = mid + 1
            
            6. else: right half is sorted.
                    if my_list[high] >= target and target >= my_list[mid]:
                        eliminate left half left = mid + 1
                    else 
                        eliminate right half right  = mid - 1 
                        
                        
"""


my_list = [4,5,6,7,0,1,2]
target = 9


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
