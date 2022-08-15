/*
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

*/

function maxsubarray(nums){
    if (nums.length == 1) return nums[0]
    let maxsum = nums[0]
    let currentsum = nums[0]
    for (let i=1; i<nums.length; i++){
        currentsum = max(nums[i], currentsum+nums[i])
        if(currentsum<maxsum) maxsum = currentsum
        
    }
    return maxsum
}

// Time complexity = O(n)
// Space complexity = O(n)