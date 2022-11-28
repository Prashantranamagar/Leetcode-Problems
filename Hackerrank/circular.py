""" 
Source:https://www.hackerrank.com/challenges/circular-array-rotation/problem?isFullScreen=true

"""



def circularArrayRotation(a, k, queries):
    for i in range(k):
        a.insert(0,a[-1])
        a.pop()
    out = []
    for query in queries:
        out.append(a[query])
    return out