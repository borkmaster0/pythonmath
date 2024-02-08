import itertools
from math import *
from cmath import *

# Sets
class Sets:
    def setOps(self, set1: list, set2: list, type: str): # Performs set operations (union, intersection, set_diff, combinations)
        output = []
        if type == 'union':
            return sorted(set1.union(set2))
        
        if type == 'intersection':
            return sorted(set1.intersection(set2))
        
        if type == 'set_diff':
            return sorted(set1.symmetric_difference(set2))
        
        if type == 'combinations':
            return sorted(list(itertools.product(set1, set2)))
        
        TypeError("Not a valid operation.")
    
    def listMultiply(self, list1: list, list2: list): # Multiply 2 lists together
        output = []
        for i in list1:
            for x in list2:
                output.append(i * x)
        return output
    
    def listExp(self, list1: list, exponent: int): # Exponent a list
        out = []
        for i in list1:
            out.append(i ** exponent)
        return out
    
    def numList(self, low: int, high: int): # Create a number list
        list = []
        for i in range(low, high + 1):
            list.append(i)
        return i

# Statistics
class Stats:
    def max(self, list: list): # Gets the maximum number for the list.
        c = Controls()
        if c.emptyList(list):
            return ValueError('Empty list')
        max = list[0]
        for i in list:
            if i > max:
                max = i
        return max

    def min(self, list: list): # Gets the minimum number for the list.
        c = Controls()
        if c.emptyList(list):
            return ValueError('Empty list')
        min = list[0]
        for i in list:
            if min > i:
                min = i
        return min

    def sum(self, list: list): # Gets the sum of all the elements in the list.
        c = Controls()
        if c.emptyList(list):
            return ValueError('Empty list')
        a = 0
        for i in list:
            a += i
        return a

    def multiply(self, list: list):# Multiply.
        c = Controls()
        if c.emptyList(list):
            return ValueError('Empty list')
        a = 1
        for i in list:
            a *= i
        return a

    def average(self, list: list): # Gets the average of the list.
        return (sum(list) / len(list))

    def range(self, list: list): # Gets the range of the list.
        a = sorted(list)
        return [a[0] - a[-1]]

    def mode(self, list1: list, list2: list): #Finds all common numbers in both lists.
        a = []
        for i in list1:
            for x in list2:
                if (i == x):
                    a.append(i)
        return a

    def factorial(self, num: int): # Factorial
        g = []
        s = Stats()
        for i in range(0, num):
            g.append(i)
        return s.multiply(g)

    def ncr(self, n: int, r: int): # Combinations
        s = Stats()
        return s.factorial(n) / (s.factorial(n - r) * s.factorial(r))

    def npr(self, n: int, r: int): # Permutations
        s = Stats()
        return (s.factorial(n) / s.factorial(n - r))

    def binDist(self, x: int, n: int, p: int): # Binomial Distribution
        s = Stats()
        return s.ncr(n, x) * (p ** x) * ((1 - p) ** (n - x))

    def linReg(self, xlist: list, ylist: list): # Linear Regression
        if len(xlist) != len(ylist):
            TypeError("Not equal length")
        # Define classes
        s = Stats()
        p = Sets()
        
        n = len(xlist)
        sx = s.sum(xlist)
        sy = s.sum(ylist)
        sxy = s.sum(p.listMultiply(xlist, ylist))
        sxsq = s.sum(p.listExp(xlist, 2))
        sysq = s.sum(p.listExp(ylist, 2))
        a = ((sy * sxsq) - (sx * sxy)) / ((n * sxsq) - (sx ** 2))
        b = ((n * sxy) - (sx * sy)) / ((n * sxsq) - (sx ** 2))
        return "y= " + str(a) + "x + " + str(b)

    def normPDF(self, mean: float, stdev: float, x: float): # Normal Probability Density Function
        s = Stats()
        return ((1 / (sqrt(2 * pi * (stdev ** 2)))) * (exp((0 - ((x - mean) ** 2)) / (2 * (stdev ** 2)))))

    def variance(self, type: str, list: list): # Find the standard variance of the given data.
        s = Stats()
        mean = s.average(list)
        a, b, c = []
        for i in list:
                a.append(i - mean)
        for i in a:
            b.append(i ** 2)
        c = s.sum(b)
        if type == 'sample':
            return c / (len(list) - 1)
        else:
            return c / len(list)

