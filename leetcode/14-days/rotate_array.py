class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(len(nums)):
        #     pos = (i + k) % (len(nums))
        mod = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, mod - 1)
        self.reverse(nums, mod, len(nums) - 1)
    
    def reverse(self, nums, start, end):
        while end > start:
            temp = nums[end]
            nums[end] = nums[start]
            nums[start] = temp
            end -= 1
            start += 1