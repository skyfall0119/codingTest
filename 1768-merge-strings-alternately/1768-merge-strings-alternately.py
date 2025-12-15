class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        ind = 0
        for a, b in zip(word1, word2):
            ans.append(a)
            ans.append(b)

        ans.append(word1[len(word2):])
        ans.append(word2[len(word1):])


        
        return "".join(ans)

