import sys
sys.path += ['../../utils/']
from utils import Test

def tests(solution):
    assert solution("()")
    assert solution("()[]{}")
    assert not solution("(]")
    assert solution("([{}])")
    assert not solution("[(])")
    assert not solution("(")
    assert not solution("[")
    assert not solution("{")
    assert not solution(")")
    assert not solution("]")
    assert not solution("}")
    assert solution("[]")
    assert solution("{}")
    assert solution("({})")
    assert solution("([{({{()}})}])")
    assert solution("(([{}]){()}[({})]{}[({{[]}})])")
    assert not solution("(([{}]){()}[({))]{}[({{[]}})])")
    assert solution("(([{}]){()}[({})]{}[({{[]}})]){}()")
    assert not solution("())")
    assert not solution(")()(")
    assert not solution("(}")
    assert solution("((){}())[{{{{[()]}}}}]{[]}(({})){}[]")
    assert not solution("((){}()){[{{{{[()]}}}}]{[]}(({}})){}[]")
    assert solution("[((((([]((({}((({()((({({({({([[[[[[(){{}}[[()]]]]]]]])})})})})))}))[])))){})))))]")

def advanced_tests(solution):
    Test.template(tests, solution)
