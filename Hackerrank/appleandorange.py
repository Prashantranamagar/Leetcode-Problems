"""
Source:https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=true


"""

def countApplesAndOranges(s, t, a, b, apples, oranges):
    acount = 0
    bcount = 0
    
    for i in range(len(apples)):
        apple_distance = a + apples[i]
        if (apple_distance in range(s, t+1)):
            acount += 1
      
      
    for i in range(len(oranges)):
        oranges_distance = b + oranges[i]
        if (oranges_distance in range(s, t+1)):
            bcount += 1
    
    print (acount)
    print (bcount)
