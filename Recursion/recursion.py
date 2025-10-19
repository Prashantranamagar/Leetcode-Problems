"""
A function that calls itself until it doesnot.

"""

def open_gift_box():
    value = input("Enter the gift : ")

    if value == "ball":
        return "ball"
    open_gift_box()

# open_gift_box()


#Call Stack

def fun1():
    print("fun1")

def fun2():
    fun1()
    print('fun2')

def fun3():
    fun2()
    print('fun3')

# fun3()


#Find the factiorial of the number using recursion

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


print(factorial(4))
    