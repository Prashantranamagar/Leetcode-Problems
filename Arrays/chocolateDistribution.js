/*
Chocolate Distrubution Problem.

Source:https://www.geeksforgeeks.org/chocolate-distribution-problem/

Question:
Given an array of n integers where each value represents the number of chocolates in a packet. Each packet 
can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that: 
The difference between the number of chocolates in the packet with maximum chocolates and the packet with minimum 
chocolates given to the students is minimum.

Examples
Input : arr[] = {3, 4, 1, 9, 56, 7, 9, 12} , m = 5 
Output: Minimum Difference is 6 
Explanation: The set goes like 3,4,7,9,9 and the output is 9-3 = 6

Input : arr[] = {12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50} , m = 7 
Output: Minimum Difference is 10 
Explanation: We need to pick 7 packets. We pick 40, 41, 42, 44, 48, 43 and 50 to minimize difference between maximum 
and minimum

Two approaches:
1. Naive Approach: The idea is to generate all the subset of the given array.  
                   And find the difference between maximum and minimun elements in it.

2. Efficient Approach: Sort the array, Find the subarray of size m with the minimum difference between the last and
                       the first.

*/


//Approach 2
function choclatedisturibution(array, m) {   // m is no of student.
    let sortedarray = array.sort(function(a, b){return a - b});
    let diff = sortedarray[sortedarray.length-1] - array[0]
    for(i=0; i<sortedarray.length-m; i++){
        diff = Math.min(diff, sortedarray[i+m-1]-array[i])

    }
    return diff
}

//Time complexity = O(nlogn)  as we sort before subarray search.
//Space = O(1)