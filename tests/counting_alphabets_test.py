import sys
sys.path.append('../problems/')
from counting_alphabets import solution

# test cases
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
# done
print("ADVANCED TEST PASS")