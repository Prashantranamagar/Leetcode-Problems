"""
Minimum and maximum element in an array.
Source:https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/


"""


def min_max(my_list):  # Time Complexity: O(n) space : O(1)
    max = my_list[0]
    min = my_list[0]
    for item in my_list:
        if item > max:
            max = item
        if item < min:
            min = item
    return [max, min]

# my_list = [1, 2, 3, 9, 5, 8, 7, 6]
# print(min_max(my_list))


# alternatively
def minmax_1(my_list):  # Time complexity = O(nlog(n))
    my_list.sort()  # time complexity of .sort() method is n(logn)
    max = my_list[-1]
    min = my_list[0]
    return max, min

# my_list = [1, 2, 3, 9, 5, 8, 7, 6]
# print(minmax_1(my_list))


def minmax(arr):  # Time complexity = O(n)
    n = len(arr)
    if(n%2 == 0):
        mx = max(arr[0], arr[1])
        mn = min(arr[0], arr[1])
        i=2
    else:
        mx = mn = arr[i]
    while(i<n-1):
        if (arr[i]<arr[i+1]):
            mx = max(mx, arr[i+1])
            mn = min(mn, arr[i])
        else:
            mx = max(mx, arr[i])
            mn = min(mn, arr[i+1])
        i += 2
    return  (mx,mn)

# my_list = [1, 2, 3, 9, 5, 8, 7, 6]
# minmax(my_list)











