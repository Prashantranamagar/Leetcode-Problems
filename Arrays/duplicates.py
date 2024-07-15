# Find duplicates return the duplicates with their frequency i.e how many time it repeates.

my_list = ['a', 'b', 'c', 'a', 'b']

def Counter(my_list):
  """
  Counter function return map with value and its frequency for a given list.
  """
  counter_map ={}
  for item in my_list:
    if item not in counter_map:
      counter_map[item] = 1
    else:
      counter_map[item] += 1
  return counter_map


# or import Counter from Collections
# from collections import Counter


def duplicates_1(my_list):
  result = []
  freq_map = Counter(my_list)
  print(freq_map)
  for item in freq_map:
    if freq_map[item] > 1:
        result.append((item, freq_map[item]))
  return result
    
print(duplicates_1(my_list))  # Time complexity O(n)


# def duplicates(my_list):
#     result = []
#     index_res = []
#     for item in my_list: # O(n)
#         if my_list.count(item) > 1: # O(n)
#           if item not in result:   # O(n)
#             result.append(item)
#             index = my_list.index(item) # O(n)
#             index_res.append(index)
#     return result, index_res

# Time complexity:  O(n){O(n)+O(n)+O(n)} --> O(n){3(On)}  -->O(n)*O(n) -->O(n^2) i.e. this is not optimized


# print(duplicates(my_list))