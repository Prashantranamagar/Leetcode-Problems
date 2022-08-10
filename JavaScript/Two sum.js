/*
Source:https://leetcode.com/problems/two-sum/

Question:Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Examples:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Here to solve the problem we can use two approaches since the given array is unsorted
1. Brute Force O(n^2)
   The brute force approach is simple. Loop through each element xx and find if there is another value that 
   equals to target - xtarget−x.    

2. Two-pass Hash Table O(n)
   Simply use two iterations. In first iterations we add each value element as key in the hash table.
   Then in second iteration we check if each element complement i.e (target-nums[i]) exixt in the hash table.
   If it does we return current element index and its complement index. 

*/

//Brute Force
function twoSum(nums, target){
    for(let i=0; i<nums.length; i++){
        for(let j=i+1; j<nums.length; j++){
            if (nums[i] + nums[j] == target)
            return [i,j]
        }
    }
} 


//Hash Table
function twoSum(nums, target){
    let map = {}
    for(let i=0; i<nums.length; i++){
        map[nums[i]] = i
    }
    for(j=0; j<nums.length; j++){
        let complement = target -nums[i]
        if (complement in map && map[complement]!== i){
            return [i, map[complement]]
        }
    }
}


// if the given array is sorted we can use binary search and the complexity will become O(logn)
function twoSum(nums, target){
    let left = 0
    let right = nums.length
    while(left<right){
        if (nums[left] +nums[right] === target){
            return [left, right]
        }
        else if(nums[left] + nums[right] > target){
            right--
        }
        else{
            left++
        }
        return [left, right]
    }
    return -1
}

