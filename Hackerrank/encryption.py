"""
Source:https://www.hackerrank.com/challenges/encryption/problem

"""


import math


def encryption(s):
    string = s.replace(" ", "")
    string_len = len(string)
    row = math.floor(math.sqrt(string_len))
    col = math.ceil(math.sqrt(string_len))
    # print(s)
   
      
    if row * col < string_len:
      row += 1
      
    # string_sep = ''
    # index=0
    # while index < len(string):
    #     string_sep = string_sep + '' + string[index:index+col]
    #     index = index + col
    # # print(string_sep)    
      
      
    result = ''
    for i in range(col):
      j = 0
      while (i+j < string_len):
        result += string[i+j]
        j+=col
      result+=' '

    return result

# encryption('feedthedog')