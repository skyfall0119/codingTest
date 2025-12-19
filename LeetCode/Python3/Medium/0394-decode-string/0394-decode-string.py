class Solution:

    def decode(self, s,e):
        print("decode", self.li[s:e+1])
        print(s,e)
        if s > e:
            print("out")
            return ""
        
        ret = []

        left_stack = []
        state = "normal"

        repeat = 0
        for i in range(s,e+1):
            if state == "normal":
                if not self.li[i].isdigit():
                    ret.append(self.li[i])
                else:
                    repeat = int(self.li[i])
                    state = "num"
                

            elif state == "num":
                if self.li[i] != "[":
                   repeat = repeat*10 + int(self.li[i])
                else:
                   left_stack.append(i)
                   state = 'bracket'
                   

                    

            else : #bracket
                if self.li[i] == "[":
                    left_stack.append(i)
                elif self.li[i] == ']':
                    start = left_stack.pop()

                    if not left_stack: # found a full complete bracket
                        inside = self.decode(start+1,i-1) 
                        ret.append(inside * repeat)
                        state = "normal"

        return "".join(ret)

            

    def decodeString(self, s: str) -> str:
        self.li = list(s)
        return self.decode(0, len(s)-1)