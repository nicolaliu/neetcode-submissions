# [1,2,4,6]
# prefix[i] = products before nums[i]
# prefix = [1,1,2,8]
# postfix = [48,24,6,1]
# output = [48,24,12,8]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums: return []

        n = len(nums)
        output = [1] * n

        for i in range(1,n):
            output[i] = nums[i-1] * output[i-1]
        
        postfix = 1
        for i in range(n-1, -1, -1):
            output[i] = output[i] * postfix
            postfix *= nums[i] 

        return output
        