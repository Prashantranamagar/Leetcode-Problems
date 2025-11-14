"""
Bubble sorting -->
Repeatedly swaps adjacent elements if they are in the wrong order.

"""


def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0 ,-1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list

def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

list = [3, 9, 1, 4, 8]

# print(bubble_sort(list))
"""

Selection sort 
Finds the minimum element and places it at the correct position, repeating for the rest.
"""
def selection_sort(list):
    length = len(list)
    for i in range(length-1):
        start = i
        min = i
        for j in range(i+1, length):
            if list[j]<list[min]:
                min = j
        # temp = list[start]
        # list[start] = list[min]
        # list[min] = temp
        # avove three line swap in short in python beow one line code
        list[start], list[min] = list[min], list[start]
    return list

def selection_sort(list):
    n = len(list)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if list[j] < list[min_idx]:
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]
    return list

print(selection_sort(list))



"""
Insertion sort 
Builds the sorted array one element at a time by inserting each element at the correct position.

"""

def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j] 
            my_list[j] = temp
            j -= 1
    return my_list

def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i-1
        while j >= 0 and list[j] > key:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key
    return list
