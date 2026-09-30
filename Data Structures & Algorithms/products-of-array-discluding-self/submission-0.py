# [1,2,4,6]
# prefix[i] = products before nums[i]
# prefix = [1,1,2,8]
# postfix = [48,24,6,1]
# output = [48,24,12,8]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums: return []

        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n
        output = [1] * n

        for i in range(1,n):
            prefix[i] = nums[i-1] * prefix[i-1]
        
        for i in range(n-2, -1, -1):
            postfix[i] = nums[i+1] * postfix[i+1]

        for i in range(n):
            output[i] = prefix[i] * postfix[i]

        return output
        