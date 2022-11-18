import sys
sys.path += ['../../utils/']
from utils import Test

def tests(q):
    q.push(1)
    q.push(2)
    q.push(3)
    assert q.pop() == 1
    assert q.peek() == 2
    assert q.pop() == 2
    assert not q.empty()
    assert q.pop() == 3
    assert q.empty()
    assert q.pop() is None
    assert q.peek() is None
    q.push(1)
    q.push(2)
    q.push(3)
    assert q.pop() == 1
    assert q.peek() == 2
    assert q.pop() == 2
    assert not q.empty()
    q.push(3)
    assert q.pop() == 3
    assert not q.empty()
    assert q.peek() == 3
    assert q.pop() == 3
    assert q.empty()
    assert q.peek() is None
    assert q.pop() is None
    q.push(5)
    assert q.pop() == 5
    q.push(6)
    assert q.pop() == 6
    q.push(7)
    assert q.peek() == 7
    assert not q.empty()
    assert q.pop() == 7
    assert q.peek() is None
    assert q.pop() is None
    assert q.empty()

def advanced_tests(solution):
    Test.template(tests, solution)
