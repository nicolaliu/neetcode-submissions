class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        n = len(nums)
        bucket = [[] for _ in range(n+1)]

        for num, freq in count.items():
            bucket[freq].append(num)
        
        result = []
        for freq in range(len(nums), 0, -1):
            for num in bucket[freq]:
                result.append(num)
                if len(result) == k:
                    return result

