class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.search(nums, target, 0, len(nums) - 1)

    def search(self, nums, target, start, end) -> int:
        if start > end:
            return start;

        mid = start + int((end - start) / 2)
        
        if target > nums[mid]:
            return self.search(nums, target, mid + 1, end)
        if target < nums[mid]:
            return self.search(nums, target, start, mid - 1)
        return mid
        