class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if s == "":
            return True
        
        
        
        def isSubsequence_Worker(i,j):
            
            if i==len(s):
                res[0]=True
                
            else:
                
                if i<len(s) and j<len(t):
                    if s[i]==t[j]:
                        isSubsequence_Worker(i+1, j+1)

                    else:
                        isSubsequence_Worker(i, j+1)
            
            
        res=[False]
        isSubsequence_Worker(0,0)
        return res[0]
