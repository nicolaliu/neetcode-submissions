class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Check if nums is empty
        if not nums: return []

        num_by_index = dict()

        for i in range(len(nums)):
            if target - nums[i] in num_by_index:
                return [num_by_index[target-nums[i]], i]
            else:
                num_by_index[nums[i]] = i
        
        return []