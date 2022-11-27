"""
Source:https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true


"""

def miniMaxSum(arr):
    sorted_arr = sorted(arr)
    maxSum = sum(sorted_arr[1:])
    minSum = sum(sorted_arr[:-1])
    result =[minSum, maxSum]
    print(*result)
    