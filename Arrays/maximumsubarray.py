"""
Source:https://leetcode.com/problems/maximum-subarray
Examples:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Input: nums = [1]
Output: 1

Input: nums = [5,4,-1,7,8]
Output: 23

There are two approaches to solve the given problem 
    1. Brute Force approach
        Simply run nested loop over the array
    
    2. Linerar solution 
    initialize first item as max_item and current_max item
    loop over the arr or list
        current_max_item = max(ith item, current_max_item + ith item)
        if curernt_max_item > max_item:
            max_item = current_max_item
    return max_item

"""


def max_sub_array(nums):
    current_sum = nums[0]
    max_sum = nums[0]
    length = len(nums)
    for i in range(1, length):
        current_sum = max(nums[i], current_sum + nums[i])  
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum




nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sub_array(nums))





def max_subarray_with_subarray(nums):
    max_so_far = float('-inf')
    max_ending_here = 0
    start = end = s = 0

    for i in range(len(nums)):
        max_ending_here += nums[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i

        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1

    return nums[start:end + 1], max_so_far