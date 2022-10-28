/*
Source:https://www.interviewbit.com/problems/repeat-and-missing-number-array/

Examples:

Approach:
1. By sorting the array traverse the array and check for missing and repeating
2. By using mao to store numner
    Create hash table withe the help of map
    Elements are mapped to their natural index
    if element is mapped twice than it is repeating.
    if element mapping is not there it is missing.
3.Make two equations
    S = N(N+1)/2
    Sun_sq = N(N+1)(2N+1)/6

*/