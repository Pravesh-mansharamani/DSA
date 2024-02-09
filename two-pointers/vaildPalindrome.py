class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for i in s:
            if i.isalnum():
                new_str += i.lower()
        
        return new_str == new_str[::-1]

    '''We can use pointers and make it more effecient memory wise
       but the time complexity will be the same O(n)'''



