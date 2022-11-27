"""
Source:https://www.hackerrank.com/challenges/kaprekar-numbers/problem?isFullScreen=true

"""

def kaprekarNumbers(p, q):
    output = []
    
    for i in range(p,q+1):
        sq_num = i*i
        sq_num_str = str(sq_num) 
        sq_num_len = len(sq_num_str)
        
        if sq_num_len == 1:
            if i == sq_num:
                output.append(i)
        else:   
            first_half = int(sq_num_str[:sq_num_len//2])
            second_half = int(sq_num_str[sq_num_len//2:])
            result = first_half + second_half
            if i == result:
                output.append(i)
    if len(output) == 0:
        print('INVALID RANGE')
    else:
      print(*output)