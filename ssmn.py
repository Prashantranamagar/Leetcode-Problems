"""
Question: Find the second smallest missing number in a given array.

For Example :

array = [5, 8, 9, 4, 1, 3] 

result = 6

"""

# Solution 1
def ssmn(array):
    array.sort()
    for i in range(0, len(array)-1):
        if i+1 != array[i]:
            array.append(i+1)
            break
    array.sort()
    print(array)
    
    for i in range(0, len(array)-1):
        if i+1 != array[i]:
            return i+1

# Solution 2
def ssmn(list):
    list.sort()
    print(list)
    i = 0
    count = 0
    length = len(list) - 1
    print(i, length)
    while i < length:
        print('a')
        if list[i] == i + 1 + count:
            print(list[i], i + 1 + count)
            i += 1
        else:
            count += 1
        print(count)
        print(i)
        if count == 2:
            return i + count


print(ssmn([5, 8, 9, 4, 1, 3]))
