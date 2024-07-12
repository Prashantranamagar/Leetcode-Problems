"""
    Quesion no 1
    Given a list on random integer number.
    Find the  number that is repeated maximum time and also find the index of
    the first occurance of the max repeated number.   
"""

"""
    Apporach:
    Initialize an empty dictonary.
    Loop over the given list.
    add the the dictonay with the numbers from the list and with its frequency.
"""

def Counter(my_list):
    """
    counter utility function for generating dictionary
    with each element count from given list.
    """
    counter = {}
    for item in my_list:
        if item not in counter:
            counter[item] = 1
        else:
            counter[item] += 1
    return counter


# you can also import the same counter function form collection which is
# a python built in module. eg from collection import Counter
# from collections import Counter
# print(Counter(my_list)


def get_max_freq_item_with_first_occer_index(my_list):
    counter = Counter(my_list)
    max_freq_value = None
    for item in counter:
        if counter[item] == max(counter.values()):
            max_freq_value = item
            
    # first_occ = None
    # for i, item in enumerate(my_list):
    #     if item == max_freq_value:
    #         first_occ = i
    #         break

    #alernative of avbove code to find index use .index() list method
    first_occ= my_list.index(max_freq_value)

    return max_freq_value, first_occ


my_list = [1, 2, 3, 3, 3]
print(get_max_freq_item_with_first_occer_index(my_list))




"""
    Question no 2
    generate a 20 lsit of random number using list comprehension and random module
"""

import random
my_list_2 = [random.random() for i in range(20)]
print(my_list_2)



"""
    Question no 3
    You are given a list with random intege number you need sort them with first odd number and even number after that in the same list. 

    eg: my_list = [1, 2, 4, 5, 6, 7, 8]
    output = [1,5,7,2,4,6,8]

"""

# Using extra space
# my_list = [1, 10, 2, 9, 4, 5, 6, 7, 8]
# odd_list = [x for x in my_list if x % 2 != 0]
# even_list = [x for x in my_list if x % 2 == 0]
# odd_list.sort()
# even_list.sort()
# result_list = odd_list + even_list
# print(result_list)


# Without using extra space
my_list = [1, 2, 4, 5, 6, 7, 8]

i = 0
j = len(my_list)-1

while i < j:
    if my_list[i] % 2 != 0:
        i += 1
    elif my_list[j] % 2 == 0:
        j -= 1
    # If the number at the i-th index is even and the number at the j-th index is odd, swap them
    else:
        my_list[i], my_list[j] = my_list[j], my_list[i]
        i += 1
        j -= 1

print(my_list)
item_index = None
for index, item in enumerate(my_list):
    if item % 2 == 0:
        item_index = index
        break
print(item_index)

my_list[:item_index].sort()
my_list[item_index:].sort()
print(my_list)
