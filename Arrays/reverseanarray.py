"""
Reverse given array
Source: https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/

"""


def reverse(arr):
    reversed = []
    i=len(arr)-1
    while i>=0:
        reversed.append(arr[i])
        i-=1
    return reversed


def reverse_1(my_list):
    result_list = []
    length = len(my_list) - 1
    for i in range(length, -1, -1):
        result_list.append(my_list[i])
    return result_list


my_list = [1, 2, 3, 4]

print(my_list[::-1])

print(reverse(my_list))

print(reverse_1(my_list))
