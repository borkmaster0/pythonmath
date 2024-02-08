import itertools
from math import *
from cmath import *

# Number Functions
class Number:
    
    def factor(self, num: int): # Factors a number.
        numList = []
        keepList = []
        for i in range(1, num):
            numList.append(i)
        for x in range(1, len(numList)):
            if (num % x) == 0:
                keepList.append(x)
        return set(keepList)

    def isEven(self, num: int): # Checks if a number is even.
        if num % 2 == 0:
            return True
        else:
            return False

    def isPrime(self, num: int): # Checks if a number is a prime.
        if num == 1:
            return False
        elif num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return False
            return True

    def isInt(self, num): # Checks if a number is an integer.
        return (round(num) == 1)

    def sign(self, num: int): # Reports the sign of a number.
        return 1 if num > 1 else 0 if num == 0 else -1

    def isNegative(self, num: int): # Checks if a number is negative.
        return (self.sign(num) == -1)

    def isWhole(self, num: float): # Checks if a number is a whole number.
        return (ceil(num) == num) or (floor(num) == num)

    def divWithRem(self, num1: int, num2: int): # Divides the numbers and reports the remainder, if there is one.
        if num1 < num2:
            return 0
        if num2 == 0:
            ZeroDivisionError
        if (num1 % num2) == 0:
            return num1 / num2
        else:
            return str(floor(num1 / num2)) + ' r ' + str(num1 % num2)

    def gcf(self, num1: int, num2: int): # Finds the GCF of 2 numbers.
        t = Sets()
        return list(t.setOps(self.factor(num1), self.factor(num2), 'intersection'))[-1]

    def lcm(self, num1: int, num2: int): # Finds the LCM of 2 numbers.
        n = Number()
        return ((num1 * num2) / (n.gcf(num1, num2)))

    def tetration(self, start: int, amount: int): # Tetration function.
        a = start
        for i in range(2, amount):
            a = a ** start
        return a

    def logBase(self, num: float, base: float): # Log with base.
        if (num <= 0) or (base < 0):
            return 'Error'
        return (log(num) / log(base))

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

