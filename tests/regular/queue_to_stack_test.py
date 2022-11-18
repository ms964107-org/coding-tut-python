import sys
sys.path += ['../../utils/']
from utils import Test

def tests(s):
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.pop() == 3
    assert s.top() == 2
    assert s.pop() == 2
    assert not s.empty()
    assert s.pop() == 1
    assert s.empty()
    assert s.pop() is None
    assert s.top() is None
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.pop() == 3
    assert s.top() == 2
    assert s.pop() == 2
    assert not s.empty()
    s.push(3)
    assert s.pop() == 3
    assert not s.empty()
    assert s.top() == 1
    assert s.pop() == 1
    assert s.empty()
    assert s.top() is None
    assert s.pop() is None
    s.push(5)
    assert s.pop() == 5
    s.push(6)
    assert s.pop() == 6
    s.push(7)
    assert s.top() == 7
    assert not s.empty()
    assert s.pop() == 7
    assert s.top() is None
    assert s.pop() is None
    assert s.empty()

def advanced_tests(solution):
    Test.template(tests, solution)
