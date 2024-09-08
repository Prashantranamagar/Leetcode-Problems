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
This method is used when the conventional binary search algorithm cannot be used to solve the problem because the searchcondition is more complex than simply checking if an element is greater than or less than the middle element.

Sample Problems:
Finding the minimum or maximum element in a rotated sorted array.
Input: [4, 5, 6, 7, 0, 1, 2]
Output: 0 (minimum) or 7 (maximum)

Finding the first occurrence of an element in a sorted array.
Output: 2
Input: [1, 2, 3, 3, 3, 4, 5], target= 3

Searching for a target value in a matrix where each row and column is sorted.
Input: M= [[1, 4, 7], [2, 5, 8], [3, 6, 9]], t= 5
Output: True


### ISLAND MATRIX TRAVERSAL
Application:
It is used to solve problems that involve traversing a matrix or grid to find a specific pattern or object. This method is used when
the problem requires identifying clusters or groups of cells in the matrix that meet certain criteria.

DSA Used 
Matrix, queue

Sample Problems
Counting the number of islands in a
binary matrix.
Input: [[1, 1, 0, 0, 0],
[1, 1, 0, 0, 0],
[0, 0, 1, 0, 0],
[0, 0, 0, 1, 1]]
Output: 3

Finding the longest path in a matrix with
given constraints.
Input: [[5, 6, 7], [4, 9, 8], [3, 2, 1]]
Output: [9, 8, 7, 6, 5, 4, 3, 2, 1]

Finding the largest sub-matrix with all 1's.
Input: [[1, 1, 0, 1, 0],
[0, 1, 1, 1, 0],
[1, 1, 1, 1, 0],
[0, 1, 1, 1, 1]]
Output: [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]


### Two Heaps
The Two Heaps is a popular method for
solving problems that involve managing and
processing elements in two separate heaps
simultaneously. It is used when the problem
requires maintaining two sets of elements
with specific ordering or prioritization
properties.

DSA Usages:
Heap, Array

Sample Problems:
Find the median of streaming data.
Input: [2, 5, 1, 3, 6, 4]
Output: [2, 3.5, 2, 2.5, 3, 3.5]

Find the kth smallest element in an array.
Input: [3, 7, 1, 4, 5, 2] and k = 3
Output: 3

Given a continuous stream of data and a
window size, process the data efficiently
Input: [4, 1, 3, 2, 5], window size = 3
within the sliding window.
Output: [4, 4, 4, 3, 5]


### Top ‘K’ Elements
The Top 'K' Elements is a popular method for solving problems that involve finding or managing the K largest or smallest elements from a collection of elements. It is used when
the problem requires identifying the elements with the highest or lowest values based on a specific criterion.

DSA Usages:
Heap, Array

Sample Problems:
Maximum distinct elements after removing k elements.
Input: [5, 7, 5, 5, 1, 2, 2], K = 3
Output: 4

Find the top 'K' frequent elements in an
array.
Input: [3, 7, 1, 4, 5, 2] = 3
Output: 3

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0)
Input: [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
