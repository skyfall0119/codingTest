class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        cnt = 0

        # initial vowel count
        for i in range(k):
            if s[i] in vowels:
                cnt += 1

        max_num = cnt
        left_ind = 1
        while left_ind + k -1  < len(s):
            if s[left_ind + k-1] in vowels: # right
                cnt+=1
            if s[left_ind-1] in vowels: # left
                cnt -= 1
            # move
            left_ind += 1
            

            max_num = max(max_num, cnt)
        return max_num

