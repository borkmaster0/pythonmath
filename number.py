# Number Functions

from math import *
from cmath import *

def factor(num: int): # Factors a number.
    numList = []
    keepList = []
    for i in range(1, num):
        numList.append(i)
    for x in range(1, len(numList)):
        if (num % x) == 0:
            keepList.append(x)
    return set(keepList)

def isEven(num: int): # Checks if a number is even.
    if num % 2 == 0:
        return True
    else:
        return False

def isPrime(num: int): # Checks if a number is a prime.
    if num == 1:
        return False
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True

def isInt(num): # Checks if a number is an integer.
    return (round(num) == 1)

def sign(num: int): # Reports the sign of a number.
    return 1 if num > 1 else 0 if num == 0 else -1

def isNegative(num: int): # Checks if a number is negative.
    return (sign(num) == -1)

def isWhole(num: float): # Checks if a number is a whole number.
    return (ceil(num) == num) or (floor(num) == num)

def divWithRem(num1: int, num2: int): # Divides the numbers and reports the remainder, if there is one.
    if num1 < num2:
        return 0
    if num2 == 0:
        ZeroDivisionError
    if (num1 % num2) == 0:
        return num1 / num2
    else:
        return str(floor(num1 / num2)) + ' r ' + str(num1 % num2)

def gcf(num1: int, num2: int): # Finds the GCF of 2 numbers.
    from sets import setOps
    return list(setOps(factor(num1), factor(num2), 'intersection'))[-1]

def lcm(num1: int, num2: int): # Finds the LCM of 2 numbers.
    from number import gcf
    return ((num1 * num2) / (gcf(num1, num2)))

def tetration(start: int, amount: int): # Tetration function.
    a = start
    for i in range(2, amount):
        a = a ** start
    return a

def logBase(num: float, base: float): # Log with base.
    if (num <= 0) or (base < 0):
        return 'Error'
    return (log(num) / log(base))

def isBetween(num: float, low: float, high: float): # Check if number is between 2 numbers
    return (low < num) and (num < high)

