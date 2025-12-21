class Solution:
    def handle_cnt(self, chars, cnt, ind):
        for c in str(cnt):
            chars[ind] = c
            ind += 1
        return ind


    def compress(self, chars: List[str]) -> int:
        
        cur_char = ""
        cur_cnt = 0
        ind = 0

        for i in range(len(chars)):
            if i == 0:
                cur_char = chars[i]
                cur_cnt += 1
                continue
            
            if chars[i] == cur_char:
                cur_cnt += 1
            else:
                chars[ind] = cur_char
                ind += 1
                if cur_cnt > 1:
                    ind = self.handle_cnt(chars, cur_cnt, ind)
                    
                cur_char = chars[i]
                cur_cnt = 1
        
        # get last
        chars[ind] = cur_char
        ind += 1
        if cur_cnt > 1:
            ind = self.handle_cnt(chars, cur_cnt, ind)
        
        chars = chars[:ind]

        return len(chars)
                