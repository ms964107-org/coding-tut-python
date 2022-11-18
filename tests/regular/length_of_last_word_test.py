import sys
sys.path += ['../../utils/']
from utils import Test

def tests(solution):
    assert solution("Hello World") == 5
    assert solution("     Hello World") == 5
    assert solution("Hello World     ") == 5
    assert solution("Hello      World") == 5
    assert solution("   fly me   to   the moon  ") == 4
    assert solution("luffy is still joyboy") == 6
    assert solution("Hello") == 5
    assert solution("    Hello") == 5
    assert solution("Hello     ") == 5
    assert solution(" the moon  fly me to     ") == 2
    assert solution("Hi my name is blah     ") == 4

def advanced_tests(solution):
    Test.template(tests, solution)
