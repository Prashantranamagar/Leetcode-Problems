my_list = ['a', 'b', 'c', 'a', 'b']



duplicates = []
for item in my_list:
  if my_list.count(item) > 1:
    if item not in duplicates:  
      duplicates.append(item)  
print(duplicates)


output = [a, b]