class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        i = 0
        bucket = [[] for _ in range(len(nums))]
        ans = []
        while i < len(nums):
            curr = nums[i]
            temp = 0
            while i < len(nums) and curr == nums[i]:
                temp += 1
                i += 1
            bucket[temp - 1].append(curr)
        for j in range(len(bucket) - 1, -1, -1):
            if k == 0:
                return ans
            for item in bucket[j]:
                ans.append(item)
                k -= 1
                
        return ans