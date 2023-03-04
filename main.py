# https://leetcode.com/problems/isomorphic-strings/?envType=study-plan&id=level-1

def is_isomorphic(s, t):
    correlations = dict()

    for i in range(len(s)):
        try:
            if correlations[s[i]] != t[i]:
                return False
        except KeyError:
            if t[i] in correlations.values():
                return False
            else:
                correlations[s[i]] = t[i]

    return True
    

print(is_isomorphic('egg', 'add'))
print(is_isomorphic('foo', 'bar'))
print(is_isomorphic('paper', 'title'))

# -------------------------------------------------------------------------------

# Accepted LeetCode Solution:

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        correlations = dict()

        for i in range(len(s)):
            try:
                if correlations[s[i]] != t[i]:
                    return False
            except KeyError:
                if t[i] in correlations.values():
                    return False
                else:
                    correlations[s[i]] = t[i]

        return True

# Beats 71.76% of solutions in runtime, 82.49% of solutions in memory
