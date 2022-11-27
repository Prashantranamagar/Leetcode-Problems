"""
Source:

"""
def timeConversion(s):
    result = ''
    if s[-2:] == 'AM':
        if int(s[0:2]) == 12:
            # hour = 00  
            # time=str(hour) -->'0'
            hour = '00'
            time = hour + s[2:]
            result = time[0:-2]
        else:
            result = s[0:-2]
    
    elif s[-2:] == 'PM':
        if int(s[0:2]) == 12:
            result = s[0:-2]
        
        else:
            hour = int(s[0:2]) + 12
            time = str(hour) + s[2:]
            result = time[0:-2]
    return result  


# print(timeConversion('12:40:22AM'))