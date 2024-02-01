class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
     
    '''
    There is no other easiest way to solve this, You can use HASH MAP!"
    But this more easier and techinally both are O(n)
    '''

    # solution for interviews since above one is one line :O
    def isAnagram1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmapS = {}
        hashmapT = {}

        # making the hashmaps:
        for i in range(len(s)):
            hashmapS[s[i]] = 1 + hashmapS.get(s[i], 0)
            hashmapT[t[i]] = 1 + hashmapT.get(t[i], 0)

        # now checking if they are equal    
        for i in hashmapS:
            if hashmapS[i] != hashmapT.get(i, 0):
                return False
        
        return True
    
