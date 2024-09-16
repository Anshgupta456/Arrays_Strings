class Solution:
    def myAtoi(self, s: str) -> int:
        
        ans = 0
        foundFirstChar = False
        sign = 1
        
        #remove leading spaces
        s = s.lstrip(" ")
        
        
        for i, char in enumerate(s):
            
            # assign sign only if it is first char. Break if not
            if char == "-":
                if foundFirstChar == False:
                    foundFirstChar = True
                    sign = -1
                else: break
            elif char == "+":
                if foundFirstChar == True: break
                foundFirstChar = True
            
            #if numeric, compute value.
            if char.isnumeric():
                foundFirstChar = True
                ans = ans * 10 + int(char)
            
            # stop if it is letters, dots or spaces
            elif char.isalpha() or char == "." or char == " ":
                break
        
        ans = ans * sign
        
        #check for max min clipping
        if ans < -2147483648:
            return -2147483648
        if ans >= 2147483648:
            return 2147483647
        return ans
