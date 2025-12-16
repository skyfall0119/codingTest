class Solution:
    def reverseVowels(self, s: str) -> str:
        li = []
        ind = []
        vowels = ['a', 'e', 'i', 'o', 'u']
        s = list(s)
        for i, c in enumerate(s):
            if c.lower() in vowels:
                li.append(c)
                ind.append(i)

        for i in ind:
            s[i] = li.pop()
        
        return ''.join(s)