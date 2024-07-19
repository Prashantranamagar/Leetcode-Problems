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
        In this approach we find the max(ith item , continue max sum subarray)
        [-2, 1, -3, 4, -1, 2, 1, -5, 4]   given arry 
        [-2, 1, -2, 4,  3, 5, 6,  1, 5]   finding the max(ith item , continue max sum subarray)

"""

import math


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