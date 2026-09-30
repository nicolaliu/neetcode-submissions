# nums: type, empty, negative, floats
# using a hashset to solve, time:O(N), space:O(N)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums: return False

        lookup = set()

        for num in nums:
            if num in lookup:
                return True
            else:
                lookup.add(num)
        
        return False