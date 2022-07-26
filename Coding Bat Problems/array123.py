"""

Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array 
somewhere.

Examples:
array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True

"""


def array123(nums):
  if len(nums) < 3:
    return False
  for i in range(len(nums)):
    sequencecheck = nums[i:i+3]
    if sequencecheck == [1,2,3]:
      return True
  return False
