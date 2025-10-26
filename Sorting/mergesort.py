"""
Merge sort
1. Divide the list into half
2. when len list is 1
3. use merge to put list together
Time complexity is log(n)
"""

def merge(list1, list2):
    i = 0
    j = 0
    length1 = len(list1)
    length2 = len(list2)
    combiled_list = []
    while i < length1 and j < length2:
        if list1[i] < list2[j]:
            combiled_list.append(list1[i])
            i += 1
        if list2[j] < list1[i]:
            j += 1
        
        while i < length1:
            combiled_list.append[i]
            i+=1
        while j < length2:
            combiled_list.append[j]
            j+=1
    return combiled_list


def merge_sort(mylist):
    if len(mylist) == 1;
        return mylist
    mid_index = int(len(mylist)/2)
    left = merge_sort(mylist[:mid_index])
    right = merge_sort(mylist[mid_index:])

    return merge(left, right)

