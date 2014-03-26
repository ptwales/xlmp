from operator import mul
import re

__FAIL__ = "~FAIL!"


def __stripNull(vlist):
    return [v for v in vlist if v]


def mapVal(value):
    return value


def mapSum(*valueList):
    valueList = __stripNull(valueList)
    return sum(valueList)


def mapAssert(*valueList):
    valueList = __stripNull(valueList)
    if len(valueList) == 1:
        return valueList[0]
    else:
        for i in range(0, len(valueList) - 1):
            if valueList[i] != valueList[i + 1]:
                return __FAIL__
        return valueList[0]


def mapCond(x, y, true_case, false_case):
    return true_case if x == y else false_case


def mapProd(*valueList):
    valueList = __stripNull(valueList)
    return reduce(mul, valueList, 1)


def mapRegEx_match(regular_expression, some_string):
    return re.match(regular_expression, some_string)  # double check that.


tokenDict = {
    '$': mapVal,
    '==': mapAssert,
    '+': mapSum,
    '*': mapProd,
    '?': mapCond,
    '^': mapRegEx_match
    }