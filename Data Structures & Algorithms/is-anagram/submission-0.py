class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

            
        else:
            slist = list(s)
            tlist = list(t)
            return sorted(slist) == sorted(tlist)

    
            