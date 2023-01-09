import sys
sys.path += ['../../utils/']
from utils import Test

def tests(solution):
    assert solution("add", "egg")
    assert not solution("foo", "bar")
    assert solution("paper", "title")
    assert solution("ACAB", "XCXY")
    assert not solution("ACAB", "XCXC")
    assert solution("abcdefg", "gfedcba")
    assert not solution("abcdefg", "gfadcba")
    assert solution("abcde", "negch")
    assert not solution("abcde", "negc")
    assert solution("AAHAABDDRHHC", "aahaabddrhhc")
    assert solution("AAHAABDDRHHC", "aahaabddrhhp")
    assert solution("AAHAABDDRHHC", "qqlqqhddnllo")

def advanced_tests(solution):
    Test.template(tests, solution)
