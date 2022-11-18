import sys
sys.path += ['../../utils/']
from utils import Test

def tests(solution):
    assert solution("anagram", "nagaram")
    assert not solution("rat", "car")
    assert solution("iamlordvoldemort", "tommarvoloriddle")
    assert solution("a", "a")
    assert not solution("a", "b")
    assert not solution("aa", "ab")
    assert not solution("aa", "aab")
    assert solution("ab", "ba")
    assert solution("ab", "ab")
    assert solution("DamonAlbarn", "DanAbnormal")
    assert solution("GlenDuncen", "DeclenGunn")
    assert solution("EdwardGorey", "GedrodwEary")
    assert not solution("DamosAlbarn", "DanAbnormal")
    assert not solution("GlenDudcen", "DeclenGunn")
    assert not solution("EdwardGorey", "GedroswEary")

def advanced_tests(solution):
    Test.template(tests, solution)
