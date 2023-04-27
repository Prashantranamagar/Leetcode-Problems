# Determine whether the given nuber is prime or composite
# A prime number is a positive integer greater than 1 that has no positive integer divisors other than 1 and itself
# A composite number is a positive integer greater than 1 that has more than two positive divisors. In other words, a 
# composite number is a number that is not prime.
#prime numbers 2,3,5,7
#compositive numbers 4,6,8,9

# Approach 1

# a = int(input('Enter the number'))
# def pm(a):
#   if a<2:
#     print ('nethier prime nor compositive')
  
#   elif a ==2:
#     print('Prime')
  
#   elif a>2:
#     for i in range(2, a-1):
#       if a%i == 0:
#         print('compositive')
#         break
#       else:
#         print('prime')
#         break
# pm(a)



# Approach 2
from math import sqrt
a = int(input('Enter the number'))
def poc(a):
  if a==2:
    print('prime')
  for i in range(2, int(sqrt(a))+1):
    if a%i == 0:
      print('copositive')
      break
    print('prime')
poc(a)