/*

Source:https://leetcode.com/problems/search-in-rotated-sorted-array/

Examples:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Input: nums = [1], target = 0
Output: -1

Solution:
as it is a rotated sorted array, there is a pivot. we don't know where the pivot is. when we pick the middle, either it's
left side will be sorted or right side will be sorted. first, let's check - if left side is sorted or not. When will be 
the left side sorted? when low<=mid; if it's sorted, we can apply binary search in it.  But, if left side of the middle 
is sorted we will have to check if our target element is existing there or not. For that, left should be lower or equal 
to target and mid should be higher or equal to target. if that's not the case, our target element is not there, we have 
check into other half.

Time complexity=log(n)
 */


var search = function(nums, target) {
    
    let left = 0
    let right = nums.length-1
    while(left<=right){
        let middle = Math.floor((left+right)/2)

        //checking if mid is equal to target; if it is, return mid;
        if (nums[middle]==target) return middle
			
        //check if the left part is sorted
        if (nums[left]<=nums[middle]){
            //then check if target element is there or not
            if(nusm[left]<=target && nums[middle]>=target){
                right = middle-1
            }
            // if not then we have to find target into the other half, low will mid + 1
            else{
                left = middle+1
            }
        }
        //if left side is not sorrted right part is sorted
        else{
            
            if(nums[middle]<= target && nums[right] >= target){
                right = middle + 1
            } 
            else{
                left = middle - 1
  
            } 
        }
    }
    //if we dont find the element return -1
    return -1
};

