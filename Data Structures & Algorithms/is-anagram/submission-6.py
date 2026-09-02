class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #hashTable
        countS = {}
        countT={}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        return countS == countT

        #using ord(ascii value)
        count = [0] * 26

        for i in range(len(s)):
            count[ord[s[i]] - ord[s['a']]] = +1
            count[ord[t[i]] - ord[t['a']]] = -1

        for i in count:
            if i != 0:
                return False
            return True 

        

        