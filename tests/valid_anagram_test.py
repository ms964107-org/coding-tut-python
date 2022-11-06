import sys
sys.path.append('../problems/')
from valid_anagram import solution

# test cases
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
# done
print("ADVANCED TEST PASS")