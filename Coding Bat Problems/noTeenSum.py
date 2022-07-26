"""

No Teen Sum Problem

Source: https://codingbat.com/prob/p100347

Question: 
Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 
inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper 
"def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, 
you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same 
indent level as the main no_teen_sum().

Examples:
no_teen_sum(1, 2, 3) → 6
no_teen_sum(2, 13, 1) → 3
no_teen_sum(2, 1, 14) → 3

Goal:
    Define helper function : checks the given int is teen or not.
    if teen return 0 else return the given int
    find the sum

"""


def no_teen_sum(a, b, c):
  a =fix_teen(a)
  b = fix_teen(b)
  c = fix_teen(c)
  
  return a+b+c
  
# Helper Function checks teen or not
def fix_teen(n):
  if n == 13 or n == 14 or n == 17 or n == 18 or n == 19:
    return 0
  return n
