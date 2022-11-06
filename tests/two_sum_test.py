import sys
sys.path.append('../problems/')
from two_sum import solution

# test cases
assert solution([2,7,11,15], 9) == [0,1]
assert solution([3,3], 6) == [0,1]
assert solution([4,6], 7) == -1
assert solution([3, 5, 2, -4, 8, 11], 7) == [1,2]
assert solution([1, 2, 3, 4, 5, 6, 7], 14) == -1
assert solution([0, 0, 0, 0, 0, 0, 0, 0], 1) == -1
assert solution([6, 2, -1, 4, 8, -7, 1], 0) == [2,6]
# done
print("ADVANCED TEST PASS")