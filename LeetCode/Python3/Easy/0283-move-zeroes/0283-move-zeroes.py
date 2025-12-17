
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fillleft = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[fillleft] = nums[i]
                fillleft += 1
        
        for i in range(fillleft, len(nums)):
            nums[i] = 0
        