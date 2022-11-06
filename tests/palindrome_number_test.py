import sys
sys.path.append('../problems/')
from palindrome_number import solution

# test cases
assert solution(121)
assert not solution(-121)
assert not solution(10)
assert solution(101)
assert solution(1234567890987654321)
assert not solution(-1234567890987654321)
assert not solution(106579)
assert not solution(110511)
assert solution(123494321)
assert solution(0)
assert solution(48984)
# done
print("ADVANCED TEST PASS")