from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        # different length
        if len(word1) != len(word2):
            return False

        w1, w2 = Counter(word1), Counter(word2)
        w1v, w2v = w1.values(), w2.values()

        # should be made of same character
        for k1, k2 in zip(w1.keys(), w2.keys()):
            if k1 not in w2 or k2 not in w1:
                return False

        # number counts don't match
        for a,b in zip(sorted(w1v), sorted(w2v)):
            if a != b:
                return False

        # freely move, swap.
        return True