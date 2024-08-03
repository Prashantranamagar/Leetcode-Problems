"""
Source:https://leetcode.com/problems/valid-parentheses/

Question:Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example:
Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

Input: s = "[()[{()}]]"
Output: true

"""


def isValid(s):
    stack = []
    i = 0
    while i < len(s):
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            stack.append(s[i])
            i += 1
        else:
            if len(stack) == 0:
                return False
            c = stack[-1]
            if (s[i] == ')' and c == '(') or (s[i] == '}' and c == '{') or (s[i] == ']' and c == '['):
                stack.pop()
                i += 1
            else:
                return False

    if len(stack) == 0:
        return True


# print(isValid(s="[()[{()}]]"))


def validpar(input):
    # length = len(input)
    stack = []
    for item in input:
        if item == '(' or item == '{' or item == "[":
            stack.append(item)
        elif stack[-1] == '(' and item == ')' or stack[-1] == '[' and item == ']' or stack[-1] == '{' and item =='}':
            stack.pop()
        else:
            return False
    if len(stack) == 0:
        return True
    else:
        return False



# print(validpar(input="[()[{()}]]"))