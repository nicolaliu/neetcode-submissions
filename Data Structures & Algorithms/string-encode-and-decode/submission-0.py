class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res   

    def decode(self, s: str) -> List[str]:
        i = 0
        count = 0
        n = len(s)
        res = []
        while i < n:
            while '0' <= s[i] <= '9':
                count = count*10 + int(s[i])
                i += 1
            if s[i] == '#':
                res.append(s[i+1:i+count+1])
                i = i + count + 1
                count = 0
        return res

    

    
    
    
    
    
    
    
    
    
    

        

            

