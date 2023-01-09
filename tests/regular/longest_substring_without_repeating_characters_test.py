import sys
sys.path += ['../../utils/']
from utils import Test

def tests(solution):
    assert solution("abcabcbb") == 3
    assert solution("bbbbb") == 1
    assert solution("pwwkew") == 3
    for _ in range(100):
        string = Test.string_generator(20, False, True)
        assert solution(string) == example_solution(string)
    
def example_solution(s):
    # https://leetcode.com/problems/longest-substring-without-repeating-characters/solutions/347818/python3-sliding-window-o-n-with-explanation/
    seen = {}
    l = 0
    output = 0
    for r in range(len(s)):
        if s[r] not in seen:
            output = max(output,r-l+1)
        else:
            if seen[s[r]] < l:
                output = max(output,r-l+1)
            else:
                l = seen[s[r]] + 1
        seen[s[r]] = r
    return output
    
def advanced_tests(solution):
    Test.template(tests, solution)
