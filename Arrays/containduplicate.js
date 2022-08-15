/*

Source:https://leetcode.com/problems/contains-duplicate

Example:
Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Approach:
1.Using map  Time Complexity:O(N) Space Compexity: O(N)
    Buid a map from the given arry counting the number of times each numbers appearing.
    if a numner appears more than once return true else false

2.By sorting  Time Complexity:O(NlogN) Space Compexity: O(1)
    Sort the given array  
    loop over the array and check the nums[i] and nums[i+1] number 
    if they are equal return false else true
*/


//using map

function conatinduplicate(nums){
    let map = {}
    for(i=0; i<nums.length; i++){
        if(map[nums[i]]){
            map[nums[i]] ++
        }
        map[nums[i]] = 1
    }
    for (let i in map){
        if (map[i]>1){
            return false
        }
        return true
    }
}