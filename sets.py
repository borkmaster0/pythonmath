import itertools
from math import *
from cmath import *

# Sets

def setOps(set1: list, set2: list, type: str): # Performs set operations (union, intersection, set_diff, combinations)
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

def listMultiply(list1: list, list2: list): # Multiply 2 lists together
    output = []
    for i in list1:
        for x in list2:
            output.append(i * x)
    return output

def listExp(list1: list, exponent: int): # Exponent a list
    out = []
    for i in list1:
        out.append(i ** exponent)
    return out

def numList(low: int, high: int): # Create a number list
    list = []
    for i in range(low, high + 1):
        list.append(i)
    return i