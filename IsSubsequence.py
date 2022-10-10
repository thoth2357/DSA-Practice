

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        h = [k for i,j in enumerate(s) for k,l in enumerate(t) if l == j]
        print(h)
        # h = [i for i,j in enumerate(s) if j in t]
        # h = [i for i in s if i in t]
        # print(h)
        if s == "":
            return True
        if len(h) == 0:
            return False
        if len(h) == len(s) and -1 not in h:
            if max(h) == h[-1] and min(h) == h[0]:
                return True
            else:
                return False
        else: return False
        
                    
            

soln = Solution()
print(soln.isSubsequence("bb", "ahbgdc"))