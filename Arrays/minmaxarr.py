"""
Minimum and maximum element in an array.
Source:https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/


"""

def minmax(arr):
    n = len(arr)
    if(n%2 == 0):
        mx = max(arr[0], arr[1])
        mn = min(arr[0], arr[1])
        i=2
    else:
        mx = mn = arr[i]
    while(i<n-1):
        if (arr[i]<arr[i+1]):
            mx = max(mx, arr[i+1])
            mn = min(mn, arr[i])
        else:
            mx = max(mx, arr[i])
            mn = min(mn, arr[i+1])
        i += 2
    return  (mx,mn)
