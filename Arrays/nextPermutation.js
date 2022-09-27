/* 
Source : https://leetcode.com/problems/next-permutation/

Examples:
[1,2,3] -> [1,3,2] -> [2,1,3] -> [2,3,1] -> [3,1,2] -> [3,2,1]
[1,  5,  8,  4,  7,  6,  5,  3,  1] ->  [1,5,8,5,1,3,4,6,7]
            p-1  p       x

Algorithm:
Find the peak number from rght to left
Find next largest number to  the right of the peak
Flip peak-1 and largest number to the riht of peak
Reverse from peak to end of arry            

Hints:
To find peak rever iterate through given arry check if 
nums[i]>nums[i-1] if yes peak = i break through the loop

To of teh largest number reverse itereate through the given arry check if
nums[j]>nums[peak-1] if yes swap nums[j] and nums[peak - 1]

Reverse from peak to the end of array

*/

var nextPermutation = function(nums) {
    
    //find the peak
    let peak
    for(let i = nums.length-1; i>=0; i--){
        if (i === 0 ){
            peak = 0
        }
        if (nums[i]>nums[i-1]){
            peak = i
            break
            
        }
    }
    
    //find next largest number and swap
    for(let j = nums.length-1; j>=0; j--){
        if (nums[j]> nums[peak-1] ){
            
            //swap
            let temp = nums[j]   //nums[j] is the largest number
            nums[j] = nums[peak-1]
            nums[peak-1] = temp
            break
        }
    }
    
    //reverse
    let start = peak
    let end = nums.length-1
    while(start<end){
        let temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start ++
        end --
    }
    return nums

};
