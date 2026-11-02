class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        sdict = {}
        tdict = {}

        for i in s: 
            if i in sdict: 
                sdict[i] += 1
            else: 
                sdict[i] = 1

        for i in t: 
            if i in tdict: 
                tdict[i] += 1
            else: 
                tdict[i] = 1

        return sdict == tdict