// This is brute force. Time complexity : O(n^2)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return True
        return False



// This version uses a set. Time complexity : O(n)
    def containsDuplicate1(self, nums: List[int]) -> bool:
        hasBeenSeen = set()
        for i in nums:
            if i in hasBeenSeen:
                return True
            hasBeenSeen.add(i)
        return False


// This version uses Hash Table and its just a bit more effiecient then the one above. Time complexity : O(n)
    def containsDuplicate2(self, nums: List[int]) -> bool:
        hasBeenSeen = {}

        for i in nums:
            if i in hasBeenSeen and hasBeenSeen[i] >= 1:
                return True
            hasBeenSeen[i] = hasBeenSeen.get(i, 0) + 1
            
        return False







