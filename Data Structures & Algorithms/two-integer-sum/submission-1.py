# using hashmap to solve
# store num: its index in the hashmap
# check every time to see if target - num is already in the hasmap
# return the indices i and j

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = dict()

        for i, num in enumerate(nums):
            if (target - num) in lookup:
                return [lookup[target - num], i]
            lookup[num] = i
        