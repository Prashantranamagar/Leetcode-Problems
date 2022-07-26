"""
Caught Speeding
Source: https://codingbat.com/prob/p137202

Goal:
Return 0 if speed is <= 60,
        1 if speed is 61 <= speed <= 80, 
        and 2 if speed >= 81.
        If it's birthday, it should be substract by 5.

Examples:
caught_speeding(60, False) → 0
caught_speeding(65, False) → 1
caught_speeding(65, True) → 0

"""

def caught_speeding(speed, is_birthday):
  if is_birthday:
    speed = speed-5

  if speed <= 60:
    result = 0
  if speed >60 and speed <=80:
   result = 1

  if speed >=81:
    result = 2

  return result