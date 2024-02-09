class Solution:
    # So when I saw this question I went like oh hash map!! but then i forgot how to use it :(
    # So BRUTE FORCE :)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(0, n):
            sums = nums[i]
            for j in range(i+1, n):
                sums += nums[j]
                if sums == target:
                    ans = [i, j]
                    return ans
                else:
                    sums -= nums[j]
                    continue


    # now using hash map: O(n)
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        n = len(nums)
        for i in range(n):
            if target - nums[i] in hashmap:
                return [hashmap[target-nums[i]], i]
            else:
                hashmap[nums[i]] = i
                continue

