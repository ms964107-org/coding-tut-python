import sys
sys.path += ['../../utils/']
from utils import Test

def tests(solution):
    assert solution("ab#c", "ab#c")
    assert solution("ab##", "c#d#")
    assert not solution("a#c", "b")
    assert solution("#", "#")
    assert solution("a", "a")
    assert not solution("a", "b")
    assert solution("ab", "ab")
    assert solution("a#", "a#")
    assert solution("a#", "b#")
    assert solution("#a", "#a")
    assert solution("#ab", "#ab")
    assert not solution("#ab#d", "#ab#c")
    assert solution("#ab#", "#ab#")
    assert not solution("#a", "#b")
    assert not solution("#ab", "#ac")
    assert solution("#ab#", "#ac#")
    assert not solution("#ab#d", "#ac#e")
    assert not solution("a#ab#d", "a#ac#e")
    assert solution("a#ab#d", "a#ac#d")
    assert solution("###asd#dsf#", "##asdfg###dst#ghd###")
    assert solution("abcd####", "wxyz####")
    assert not solution("abcd###", "wxyz###")
    assert solution("abcd###", "axyz###")
    assert solution("sdafbjasdh#################dfiasd########dsf#####", "anskgjndsaklfndl#############################")
    assert solution("geee#e#ks", "gee##eeks")
    assert not solution("equ#ual", "ee#quaal#")
    assert solution("abcsd###", "addsq####b")
    assert not solution("a#b#c#d#e", "#e#d#c#b#a")
    assert solution("#a###b#c#d##ef#", "#a#b####c#d#e")

def advanced_tests(solution):
    Test.template(tests, solution)
