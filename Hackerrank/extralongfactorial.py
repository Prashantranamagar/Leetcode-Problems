"""
Source:https://www.hackerrank.com/challenges/extra-long-factorials/problem?isFullScreen=true

"""

def extraLongFactorials(n):
    result =1
    for i in range(1,n+1):
        result *= i
    print(result) 

# extraLongFactorials(25)
    