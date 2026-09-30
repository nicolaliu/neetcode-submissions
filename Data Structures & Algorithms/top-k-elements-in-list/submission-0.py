# # freq_by_num: [num: freq]
# n = 6
# bucket = [] for _ in range(n+1)
# 1, 2, 3, 4, 5, 6
# [1],[2],[3]
#  res = [2, 3]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        res = []

        # freq_by_num: [num: freq]
        freq_by_num = {}
        for num in nums:
            freq_by_num[num] = freq_by_num.get(num, 0) + 1
        
        bucket = [[] for i in range(len(nums)+1)]
        for num, freq in freq_by_num.items():
            bucket[freq].append(num)

        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
        