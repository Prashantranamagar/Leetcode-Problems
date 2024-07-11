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



