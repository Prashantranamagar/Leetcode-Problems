"""
Source:

"""
def timeConversion(s):
    result = ''
    if s[-2:] == 'AM':
        result = s[0:-2]
    
    elif s[-2:] == 'PM':
        hour = int(s[0:2]) + 12
        time = str(hour) + s[2:]
        result = time[0:-2]
    return result    