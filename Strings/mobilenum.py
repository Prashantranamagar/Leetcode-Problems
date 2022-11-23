"""
Source:https://www.geeksforgeeks.org/convert-sentence-equivalent-mobile-numeric-keypad-sequence/

Question:Convert a sentence into its equivalent mobile numeric keypad sequence.

Keypad sequence:
    1       2       3
           ABC     DEF
    4       5       6
   GHI     JKL     MNO
    7       8       9       
   PQRS    TUV     WXYZ

Approach:
For each character, store the sequence which should be obtained at its respective position in an array, i.e. for Z, store 9999. For Y, store 999. For K, store 55 and so on.
For each character, subtract ASCII value of ‘A’ and obtain the position in the array pointed 
by that character and add the sequence stored in that array to a string.
If the character is a space, store 0
Print the overall sequence.

"""

str = [
    "2", "22", "222",
    "3", "33", "333",
    "4", "44", "444",
    "5", "55", "555",
    "6", "66", "666",
    "7", "77", "777", "7777",
    "8", "88", "888",
    "9", "99", "999", "9999" 
]
input ="ABCDZ"

def printsequence(input):
    output = ""
    for i in range(len(input)):
        if input[i] == " ":
            output = output + "0"
        else:
            index = ord(input[i]) - ord("A")
            # Python ord() and chr() are built-in functions. They are used to convert a character to an int and vice versa.
            output = output + str[index]
    return output


print(printsequence(input))