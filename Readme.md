# DSA Problem Solving Patterns

Welcome to this repository! This repository aims to provide a comprehensive list of common patterns used in solving Data Structures and Algorithms problems.

## Table of Contents

- [Patterns](#patterns)
  - [Sliding Window](#sliding-window)
  - [Two Pointers](#two-pointers)
  - [Fast and Slow Pointers](#fast-and-slow-pointers)
  - [Merge Intervals](#merge-intervals)
  - [Cyclic Sort](#cyclic-sort)
  - [In-place Reversal of a Linked List](#in-place-reversal-of-a-linked-list)
  - [Tree Traversal](#tree-traversal)
  - [Graph Traversal](#graph-traversal)
  - [Dynamic Programming](#dynamic-programming)
  - [Topological Sort](#topological-sort)




### Sliding Window

- It's useful when we need to find a subarray or substring that meets specific criteria, 
  like a certain sum, product, or pattern, within a fixed window size.

- This technique works well for problems with arrays, strings, or hash tables, where elements 
  are processed one by one within a fixed window.

- Data Structures Involved: Array, String, HashTable

- Problems
  - Maximum or minimum Sum Subarray of Size K
    Input: [1, 4, 2, 10, 2, 3, 1, 0], k=3
    Output: 15
  - Longest Substring Without Repeating Characters
    Input: "abcabcbb"
    Output: "abc"
  - Counting distinct elements in a fixed-size window:
  - Finding the first occurrence of a pattern or substring in a string


- Solution
  - To use the sliding window pattern, we first initialize the start and end pointers to the beginning of the array. 
    Then, we iterate through the array and update the window by moving the end pointer forward until the window meets the desired conditions. 
    Once the window is valid, we can perform any necessary operations on the elements within the window, such as calculating the sum or finding the minimum element.

  - After performing these operations, we can then move the start pointer forward to "slide" the window along the array and repeat 
    the process until we have covered the entire array.


### Two Pointer and Iteratror 
- used in scenarios where the data is linear, such as arrays, strings, or linked lists.
- find pairs or subarrays in an array that satisfy a certain condition, or when we need to find a specific
  element in a sorted array.
- Typically, the two pointers advance towards opposite ends of the data structure with a fixed increment.

- Problems
  - Target Sum
    Input: [3, 5, 2, 8, 11], target = 10
    Output: [2, 8]

  - longest substring in a string that is a palindrome.
    Input: "babad"
    Output: "bab"
  
  - maximum sum sub-array
    Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    Output: [4, -1, 2, 1]

  - intersection of two sorted arrays.
    Input: [1, 3, 4, 5, 7], [2, 3, 5, 6]
    Output: [3, 5]




### Fast and Slow Pointer
- to solve problems that involve linked lists, arrays, or other data structures where we need to iterate through the data in a specific way.
- involves using two pointers - a "slow" pointer and a "fast" pointer. The slow pointer moves one step at a time, while the fast pointer moves
  two steps at a time.

  - Problems
    Detecting cycles in a linked list.
      Input: 1 -> 2 -> 3 -> 4 -> 5 -> 2
      Output: True
    Finding the middle element of a linked
    list.
      Input: 1 -> 2 -> 3 -> 4 -> 5
      Output: 3
    Finding the intersection point of two
    linked lists.
      Input: 1 -> 2 -> 3 -> 4 -> 5, 8 -> 4 -> 5
      Output: 4
    Finding the kth to last element in a linked
    list.
      Input: 1 -> 2 -> 3 -> 4 -> 5, k = 2
      Output: 4


### Merge Intervals
- The Merge Interval is a popular method for solving problems that involve merging or overlapping intervals. It is used when the problem requires combining or merging
  intervals that share a common overlap or intersection.
- DSA Usages:
  - Array, Heap
- Sample Problems:
    Given a collection of intervals, merge all
    overlapping intervals.
    Input: [[1, 3], [2, 6], [8, 10], [15, 18]]
    Output: [[1, 6], [8, 10], [15, 18]]
    
    Given a list of meeting intervals,
    determine the minimum number of
    meeting rooms required to schedule all
    the meetings.
    Input: [[0, 30], [5, 10], [15, 20]]
    Output: 2
    
    Given a set of intervals, find the union of
    all the intervals. The union is defined as
    the set of intervals that covers all the
    points in the input intervals.
    Input: [[1, 3], [2, 4], [5, 7], [6, 8]]
    Output: [[1, 4], [5, 8]]

    Conflicting Appointments

    Minimum Meeting Rooms

### 4. In-place Reversal of a LinkedList
It is used when we need to reverse the order of the elements in the linked list without using any additional data structures such as arrays or other lists.
DSA Usages:
Linked List

Sample Problems:
Reversing a linked list of any size.
Input: 1->2->3->4->5
Output: 5->4->3->2->1

Reversing a linked list from a certain point
Input: 1->2->3->4->5, lenght= 3
Output: 1->2->5->4->3
to the end.

Checking if a linked list is a palindrome.
Input: 1->2->3->2->1
Output: True

### 5. Modified Binary Search
