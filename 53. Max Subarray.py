#53 Maximum Subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        stored_sum = nums[0]
        current_sum = nums[0]
        #loop through array and keep track of max current sum
        #and stored sum
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            stored_sum = max(stored_sum, current_sum)
        return stored_sum
