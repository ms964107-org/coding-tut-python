import sys
sys.path += ['../../utils/']
from utils import Test

def tests(solution):
    assert solution("Hello World") == 'l'
    assert solution("Hello") == 'l'
    assert solution("    Hello") == 'l'
    assert solution("Hello     ") == 'l'
    assert solution("HelllllllLLLLLohhhh") == 'l'
    assert solution("   fly me   to   the moon  ") == 'o'
    assert solution("fly me   to   the moon  ") == 'o'
    assert solution("   fly me   to   the moon") == 'o'
    assert solution("luffy is still joyboy") == 'l' or solution("luffy is still joyboy") == 'y'
    assert solution("HHHHHHHHlloo       ") == 'H'

def advanced_tests(solution):
    Test.template(tests, solution)
