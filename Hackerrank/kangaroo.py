"""
Source:https://www.hackerrank.com/challenges/kangaroo/problem?isFullScreen=true

"""

def kangaroo(x1, v1, x2, v2):
    for i in range(1, 10000000):
        x1 = x1 + v1
        x2 = x2 + v2
        if x1 == x2:
            return "YES"
    return "NO"


