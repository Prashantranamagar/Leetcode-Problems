"""
Question: Check weather the given number is prime or not.
Prime No --> 1, 2 , 3, 5, 7, ... 
"""

def abc(num):
  if num == 0 or num ==1 or num ==2:
      return True
    
  for i in range(2, num):
    if num % i == 0:
      return False
    else:
      return True

# print(abc(4)) --> False