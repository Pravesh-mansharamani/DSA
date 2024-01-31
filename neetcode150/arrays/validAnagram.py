class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
     
    '''
    There is no other easiest way to solve this, You can use HASH MAP!"
    But this more easier and techinally both are O(n)
    '''

    
