class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)

        left, right = 0, total

        for i in range(len(nums)):
            
            # edge
            if i-1 < 0:
                left, right = 0, total - nums[i]
            elif i+1 == len(nums):
                left, right = total - nums[i], 0
            else:
                left += nums[i-1]
                right -= nums[i]
            if left == right:
                return i
            
        return -1        