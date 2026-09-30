class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums: return False
        
        num_by_count = {}
        for num in nums:
            if num in num_by_count:
                return True
            else:
                num_by_count[num] = 1
        return False
