
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 1

        while l <= r and r < len(nums):
            print(f"l {l} | r {r}")
            if nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r+=1
            elif nums[l] == 0 and nums[r] == 0:
                r += 1
            elif nums[l] != 0 and nums[r] != 0:
                l+=1
                r+=1
            elif nums[l] != 0 and nums[r] == 0:
                l += 1
        
        