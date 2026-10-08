class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p1 = [1] * n
        p2 = [1] * n

        for i in range(1,n):
            p1[i] = p1[i-1] * nums[i-1]
        
        for i in range(n-1, 0, -1):
            p2[i-1] = p2[i] * nums[i]

        res = [1] * n
        for i in range(n):
            res[i] = p1[i] * p2[i]
        
        return res
