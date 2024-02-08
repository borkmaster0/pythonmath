from math_lib import *

# Various Control Functions
class Controls:
    
    def getType(self, thing): # Get the type of the input.
        x = type(thing)
        if x is str:
            return 'str'
        elif x is int:
            return 'int'
        elif x is float:
            return 'float'
        elif x is complex:
            return 'complex'
        elif x is list:
            return 'list'
        elif x is tuple:
            return 'tuple'
        elif x is range:
            return 'range'
        elif x is dict:
            return 'dict'
        elif x is set:
            return 'set'
        elif x is frozenset:
            return 'frozenset'
        elif x is bool:
            return 'bool'
        elif x is bytes:
            return 'bytes'
        elif x is bytearray:
            return 'bytearray'
        elif x is memoryview:
            return 'memoryview'
        else:
            return 'NoneType'

    def emptyList(self, list: list): # Check if there is a empty list.
        return True if len(list) == 0 else False

    def IF(self, boolean: bool, ifTrue, ifFalse): # If function
        if boolean:
            return ifTrue
        else:
            return ifFalse
