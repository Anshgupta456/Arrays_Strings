class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        strt = 0 #start index
        end = len(nums) - 1 #end index
        mid = 0 #stores the middle of the array
        while strt <= end:
            mid = strt + (end - strt)//2 #find middle of range of interest
            if target == nums[mid]: 
                return mid
            if target < nums[mid]: #target can only be in the first half 
                end = mid - 1 #adjust range to exclude the second half
            elif target > nums[mid]: #target can only be in the second half 
                strt = mid + 1 #adjust range to exclude first half
        return strt #not in array, but start is intended index