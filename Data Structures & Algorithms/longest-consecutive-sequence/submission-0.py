class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        if not nums: return max_len

        numSet = set(nums)

        for num in nums:
            if num - 1 not in set(nums):
                length = 1
                while num + 1 in set(nums):
                    num += 1
                    length += 1
                max_len = max(max_len, length)

        return max_len
                
