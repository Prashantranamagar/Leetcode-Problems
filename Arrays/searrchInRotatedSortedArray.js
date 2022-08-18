/*

Source:https://leetcode.com/problems/search-in-rotated-sorted-array/

Examples:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Input: nums = [1], target = 0
Output: -1


Time complexity=logn
 */


var search = function(nums, target) {
    //use binary search
    let left = 0
    let right = nums.length-1
    while(left<=right){
        let middle = Math.floor((left+right)/2)

        if (nums[middle]==target) return middle
        if (nums[left]<=nums[middle]){
            if(target<nums[left] || target>nums[middle]){
                left = middle+1
            }else{
                right = middle-1
            }
        }else{
            
            if(target > nums[right] || target < nums[middle]){
                right = middle - 1
            } 
            else{
                left = middle + 1
  
            } 
        }
    }
    return -1
};

