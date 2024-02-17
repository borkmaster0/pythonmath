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

def median(list: list): # Find the median of the list
    from controls import emptyList
    from number import even
    if emptyList(list):
        return ValueError('Empty list')
    sortedList = sorted(list)
    
    n = len(list)
    c = []
    d = n / 2
    
    if even(n):
        c.append(list[d])
        c.append(list[d + 1])
        return (sum(c) / 2)
    else:
        c.append(list[ceil(d)])
        return c[0]

def distribution(list: list): # Find the distribution of the list
    d = {}
    for i in list:
        if d.get(i):
            d[i] += 1
        else:
            d[i] = 1
    return d

def midrange(list: list): # Find the midrange
    a = sorted(list)
    return ((a[0] + a[-1]) / 2)

def quartiles(list: list, fancyOut: bool=False): # Find the quartiles
    from controls import join
    med = median(list)
    length = len(list)
    sort = sorted(list)
    q1, q3 = []
    for i in range(0, ((length / 2) + 1)):
        q1.append(sort[i])
    for k in range(length, ((length / 2) + 1)):
        q3.append(sort[k])
    q1 = median(q1)
    q2 = median(sort)
    q3 = median(q3)
    if fancyOut:    
        return join(['Q1: ', sort[0], '-', q1, '\nl', 'Q2: ', q1, '-', q2, '\nl', 'Q3: ', q2, '-', q3, '\nl', 'Q4: ', q3, '-', sort[-1]])
    else:
        return [sort[0], q1, q2, q3, sort[-1]]

def iqr(list: list): # Find the interquartile range
    from controls import join
    med = median(list)
    length = len(list)
    sort = sorted(list)
    q1, q3 = []
    for i in range(0, ((length / 2) + 1)):
        q1.append(sort[i])
    for k in range(length, ((length / 2) + 1)):
        q3.append(sort[k])
    q1 = median(q1)
    q3 = median(q3)
    return q3 - q1

def fence(list: list): # Finds the fence of the list
    a = quartiles(list, False)
    q1 = a[1]
    q3 = a[3]
    i = iqr(list)
    lower = q1 - (i * 1.5)
    upper = q3 + (i * 1.5)
    return [lower, upper]

def outliers(list: list): # Finds the outliers of the list
    from number import isBetween
    from controls import emptyList
    a = fence(list)
    lower = a[0]
    upper = a[1]
    outliers = []
    for i in range(len(list)):
        if not(isBetween(list[i], lower, upper)):
            outliers.append(list[i])
    if emptyList(outliers):
        return None
    else:
        return outliers

def sumOfSquares(list: list): # Finds the sum of squares for the list.
    from controls import emptyList
    if emptyList(list):
        ValueError('Empty list')
    mean = average(list)
    a = []
    for i in range(0, len(list)):
        a.append((list[i] - mean) ** 2)
    return sum(a)

def mad(list: list):# Finds the mean absolute deviation.
    from controls import emptyList
    if emptyList(list):
        ValueError('Empty list')
    n = len(list)
    mean = average(list)
    a = []
    for i in range(0, n):
        a.append(abs(list[i] - mean))
    a = sum(a)
    return a / n

def xlist(low: int, high: int, step: int=1):# Generate x values for a table
    output = []
    for i in range(low, high, step):
        output.append(i)
    return output

def ylist(low: int, high: int, step: int, equation: str):# Generste y value for a function
    output = []
    eqn = lambda x: equation
    for i in range(low, high, step):
        output.append(eqn(i))
    return output

def table(a: list, b: list):# Formats x and y values to standard form
    return [a, b]