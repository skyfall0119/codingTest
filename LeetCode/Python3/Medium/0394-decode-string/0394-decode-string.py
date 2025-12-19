class Solution:

    def decode(self, li:list):
        if not li:
            return []
        
        ret = []

        left_stack = []
        state = "normal"

        num_start = 0
        repeat = 1
        for i in range(len(li)):
            if state == "normal":
                if not li[i].isdigit():
                    ret.append(li[i])
                else:
                    num_start = i
                    state = "num"
                

            elif state == "num":
               if li[i] == "[":
                  repeat = int("".join(li[num_start:i]))
                  left_stack.append(i)
                  state = "bracket"
                    

            else : #bracket
                if li[i] == "[":
                    left_stack.append(i)
                elif li[i] == ']':
                    start = left_stack.pop()

                    if not left_stack: # found a full complete bracket
                        inside = self.decode(li[start+1:i]) 
                        ret.append(inside * repeat)
                        state = "normal"

        return "".join(ret)

            

    def decodeString(self, s: str) -> str:
        return self.decode(list(s))