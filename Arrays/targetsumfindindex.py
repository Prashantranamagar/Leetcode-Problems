"""
Example
Input: my_list = [4, 8, 6, 2, 1], target_sum = 7
Output: [2, 4]

Solution:
1.Brute Force Nested loop (n^2)
2.Sort and use binary serch O(nlogn)
3.

"""




def targetsum(my_list, target_sum):  # Time complexity = O(n)
    length = len(my_list)
    map = {}
    for i in range(0, length):
        complement = target_sum - my_list[i]
        if complement in map:
            return [map[complement], i]
        map[my_list[i]] = i


my_list = [4, 8, 6, 2, 1]
target_sum = 7

print(targetsum(my_list, target_sum))