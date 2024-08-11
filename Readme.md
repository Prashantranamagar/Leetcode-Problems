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
-  used in scenarios where the data is linear, such as arrays, strings, or linked lists.
- find pairs or subarrays in an array that satisfy a certain condition, or when we need to find a specific
  element in a sorted array.
- Typically, the two pointers advance towards opposite ends of the data structure with a fixed increment.

