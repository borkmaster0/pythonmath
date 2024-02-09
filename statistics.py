import itertools
from math import *
from cmath import *

# Statistics
def max(list: list): # Gets the maximum number for the list.
    from controls import emptyList
    if emptyList(list):
        return ValueError('Empty list')
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max

def min(list: list): # Gets the minimum number for the list.
    from controls import emptyList
    if emptyList(list):
        return ValueError('Empty list')
    min = list[0]
    for i in list:
        if min > i:
            min = i
    return min

def sum(list: list): # Gets the sum of all the elements in the list.
    from controls import emptyList
    if emptyList(list):
        return ValueError('Empty list')
    a = 0
    for i in list:
        a += i
    return a

def multiply(list: list):# Multiply.
    from controls import emptyList
    if emptyList(list):
        return ValueError('Empty list')
    a = 1
    for i in list:
        a *= i
    return a

def average(list: list): # Gets the average of the list.
    return (sum(list) / len(list))

def range(list: list): # Gets the range of the list.
    a = sorted(list)
    return [a[0] - a[-1]]

def mode(list1: list, list2: list): #Finds all common numbers in both lists.
    a = []
    for i in list1:
        for x in list2:
            if (i == x):
                a.append(i)
    return a

def factorial(num: int): # Factorial
    g = []
    for i in range(0, num):
        g.append(i)
    return multiply(g)

def ncr(n: int, r: int): # Combinations
    return factorial(n) / (factorial(n - r) * factorial(r))

def npr(n: int, r: int): # Permutations
    return (factorial(n) / factorial(n - r))

def binDist(x: int, n: int, p: int): # Binomial Distribution
    return ncr(n, x) * (p ** x) * ((1 - p) ** (n - x))

def linReg(xlist: list, ylist: list): # Linear Regression
    if len(xlist) != len(ylist):
        TypeError("Not equal length")
    from sets import listMultiply, listExp

    n = len(xlist)
    sx = sum(xlist)
    sy = sum(ylist)
    sxy = sum(listMultiply(xlist, ylist))
    sxsq = sum(listExp(xlist, 2))
    sysq = sum(listExp(ylist, 2))
    a = ((sy * sxsq) - (sx * sxy)) / ((n * sxsq) - (sx ** 2))
    b = ((n * sxy) - (sx * sy)) / ((n * sxsq) - (sx ** 2))
    return "y= " + str(a) + "x + " + str(b)

def normPDF(mean: float, stdev: float, x: float): # Normal Probability Density Function
    return ((1 / (sqrt(2 * pi * (stdev ** 2)))) * (exp((0 - ((x - mean) ** 2)) / (2 * (stdev ** 2)))))

def variance(type: str, list: list): # Find the standard variance of the given data.
    mean = average(list)
    a, b, c = []
    for i in list:
            a.append(i - mean)
    for i in a:
        b.append(i ** 2)
    c = sum(b)
    if type == 'sample':
        return c / (len(list) - 1)
    else:
        return c / len(list)