class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        #init
        max_avg = 0
        sums = 0
        for i in range(k):
            sums += nums[i]
        max_avg = sums

        # loop
        for i in range(1, len(nums)-k+1):
            sums = sums - nums[i-1] + nums[i+k-1]
            max_avg = max(sums, max_avg)

        return max_avg /k