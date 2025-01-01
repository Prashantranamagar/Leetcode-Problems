
# my_list = [5, 4, 8, 2, 5, 8, 9, 8]

# counter = {}
# for item in my_list:
#     if item not in counter:
#         counter[item] = 1
#     else:
#         counter[item] += 1
# print(counter)


# max_frequency = max(counter.values())
# print(max_frequency)
# max_frequency_val = None

# for item in counter:
#     if counter[item] == max_frequency:
#         max_frequency_val = item
# print(max_frequency_val)
# result = my_list.index(max_frequency_val)
# print(result)



# Generate al list of random number using list comprehension
# import random

# random_num_list = [random.randint(5, 1000) for i in range(10)]
# print(random_num_list)




#sort odd aand then even number in a list without using extra space

# my_list = [1, 2, 4, 5, 6, 7, 8]

# i = 0
# j = len(my_list)-1

# while i < j:
#     if my_list[i] % 2 != 0:
#         i += 1
#     elif my_list[j] % 2 ==0:
#         j -= 1
#     else:
#         my_list[i], my_list[j] = my_list[j], my_list[i]


# index = None
# print(my_list)
# for i, item in enumerate(my_list):
#     if item % 2 == 0:
#         index = i
#         break

# print(index)
# # new_list = sorted(my_list[:index])  # this uses extra space
# my_list[:index]= sorted(my_list[:index])   #it doesnot use extra space it refrence to sliced portion of the list
# my_list[index:]= sorted(my_list[index:])

# print(my_list)




#####################################################################################################################
######### TWO SUM PROBLEM ##########
#####################################################################################################################
nums = [2,7,11,15]
target = 9

## Two sum problem.

# nums = [2,7,11,15]
# target = 9

# def two_sum(nums, target):
#     map = {}
#     for index, value in enumerate(nums):
#         # print(index, value)
#         complement = target - value
#         if complement in map.keys():
#             print('hello')
#             return [map[complement], index]
#         map[value] = index
#         # print(map)
#     return []
    
# print(two_sum(nums, target))



# def two_sum(nums, target):
#     map = {}
#     for index, value in enumerate(nums):
#         map[value] = index
#     for item in map.keys():
#         complement = target - item
#         if complement in map.keys():
#             return [map[item], map[complement]]


# def two_sum(nums, target):
#     map ={}
#     for index, item in enumerate(nums):
#         complement = target - item
#         # print(map)
#         if complement in map.keys():  #time complexity is (O(1))
#             # print('hjjjj')
#             return [index, map[complement]]
#         map[item] = index


# def two_sum(nums, item):
#     map = {}
#     for index, item in enumerate(nums):
#         map[item] = index
#     for item in nums:
#         complement = target - item
#         if complement in map.keys():
#             return [map[complement], index]        

# print(two_sum(nums, target))





#####################################################################################################################
######### GENERATE A LIST OF RANDOM NUMBER USING LIST COMPREHENTION ##########
#####################################################################################################################


# import random
# # print(random.randint(0,10))
# my_list = [random.randint(0, 10) for i in range(0, 10) ]
# print(my_list)



#####################################################################################################################
######### POC ##########
#####################################################################################################################
# from math import sqrt
# a = int(input('Enter the number'))
# def poc(a):
#   if a==2:
#     print('prime')
#   for i in range(2, int(sqrt(a))+1):
#     if a%i == 0:
#       print('copositive')
#       break
#     print('prime')
# poc(a)