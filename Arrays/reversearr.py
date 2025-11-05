"""
Reverse the Array
Approach 1 
use for loop to reverse arry in temp arry
Copy the temp arry in org arr

Time Complexity o(n)
Space Complexity O(n)

Approach 2: Space optimize to O(1)
Time Complexity = Same O(n)
Space Complexity O(1)
declare to pointer first index and last index
sawp the two index
fist index increment by one last index decrement by 1
sawp
continue the same 
if first_indes >= last index break:
"""
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

#Approach 1
def reverse_arr(arr):
    result = []
    length = len(arr)
    for i in range (length-1, -1, -1):
        print(i)
        print(arr[i])
        result.append(arr[i])
    arr = result
    return arr

print(reverse_arr(arr))



#Approach 2   Space O(1) time O(n)
def reverse_arr_swap(arr):
    right = 0
    left = len(arr)-1
    while right < left:
        # temp = arr[right]
        # arr[right] = arr[left]
        # arr[left] = temp
        ## in short avobve three line in one line
        arr[left], arr[right] = arr[right], arr[left]
        right +=1
        left -=1
    return arr

print(reverse_arr_swap(arr))