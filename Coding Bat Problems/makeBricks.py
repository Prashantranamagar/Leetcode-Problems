"""

Make Bricks Problems.

Source:https://codingbat.com/prob/p118406

Question: We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) 
and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given 
bricks. This is a little harder than it looks and can be done without any loops.

Goal: 
Think about the cases where goal is not possible
1.not enough bricks
2.not enough small bricks

return False if total length of brick < goal
       False if goal % 5 > small
else  return True

Examples:
make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True

"""

def make_bricks(small, big, goal):
  if 5*big + small < goal:
    return False
  a= goal % 5
  if a> small:
    return False
    
  return True
  
  
