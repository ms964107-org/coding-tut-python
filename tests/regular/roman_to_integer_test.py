import sys
sys.path += ['../../utils/']
from utils import Test

def tests(solution):
    assert solution("III") == 3
    assert solution("LVIII") == 58
    assert solution("MCMXCIV") == 1994
    for i in range(1, 4000):
        roman = integer_to_roman(i)
        assert solution(roman) == example_solution(roman)
    
def example_solution(s):
    # https://leetcode.com/problems/roman-to-integer/solutions/3016037/very-simple-python-solution/?languageTags=python3
    total = 0
    theDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in s:
        total += theDict[i]
    if "IV" in s:
        total -= 2
    if "IX" in s:
        total -= 2
    if "XL" in s:
        total -= 20
    if "XC" in s:
        total -= 20
    if "CD" in s:
        total -= 200
    if "CM" in s:
        total -= 200
    return total

def integer_to_roman(num):
    # https://leetcode.com/problems/integer-to-roman/solutions/2726348/easy-understandble-python-code-with-good-runtime/?languageTags=python3
    values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
    res=""
    for i,v in enumerate(values):
        res+=(num//v)*numerals[i]
        num%=v
    return res

def advanced_tests(solution):
    Test.template(tests, solution)
