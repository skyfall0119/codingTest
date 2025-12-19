from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1, w2 = Counter(word1), Counter(word2)

        # different length
        if sum(w1.values()) != sum(w2.values()):
            return False

        # should be made of same character
        if set(w1.keys()) != set(w2.keys()):
            return False

        # number counts don't match
        for a,b in zip(sorted(w1.values()), sorted(w2.values())):
            if a != b:
                return False

        # freely move, swap.
        return True