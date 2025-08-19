# Using stack is the best possible option and the fastest approach there is
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = { ")":"(", "}":"{", "]":"[" }
        i=0
        while i<len(s):
            if s[i] in mapping:
                if (s[i-1]!=mapping[s[i]]):
                    return False
                else:
                    if i>=1:
                        s = s[:i-1] + s[i+1:]
                        i=i-2
            i+=1
        if s!="":
            return False
        return True
