"""
Question: Find the second smallest missing number in a given array.

For Example :

array = [5, 8, 9, 4, 1, 3] 

result = 6

""" 


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


print(ssmn([5, 8, 9, 4, 1, 3] ))
            