
// Given an array of integers nums, calculate the pivot index of this array.
// The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
// If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
// Return the leftmost pivot index. If no such index exists, return -1.
//EG:
// Input: nums = [1,7,3,6,5,6]
// Output: 3
// Explanation:
// The pivot index is 3.
// Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
// Right sum = nums[4] + nums[5] = 5 + 6 = 11

// Input: nums = [2,1,-1]
// Output: 0
// Explanation:
// The pivot index is 0.
// Left sum = 0 (no elements to the left of index 0)
// Right sum = nums[1] + nums[2] = 1 + -1 = 0



var pivotIndex = function(nums) {
    let leftSum = 0 
    let rightSum = 0
    let total =0
    for( let i=0; i < nums.length; i++ ){
      total += nums[i];
    }
   for (let i=0; i < nums.length; i++){
     
     rightSum = total -leftSum - nums[i];
     if (leftSum == rightSum){
       return i
     }
    leftSum=leftSum+nums[i];
   }
    return -1;
  
  };

//Using while loop

  var pivotIndex = function(nums) {
    let leftSum = 0 
    let rightSum = 0
    let total =0
    for( let i=0; i < nums.length; i++ ){
      total += nums[i];
    }
    let i=0;
    while ( i < nums.length){
     
     rightSum = total -leftSum - nums[i];
     if (leftSum == rightSum){
       return i
     }
     leftSum=leftSum+nums[i];
     i++
   }
    return -1;
  
  };