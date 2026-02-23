#334 Increase Triplet Subsequence
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_small = float('inf')
        second_small = float('inf')
        for i in range(len(nums)):
            if(nums[i] < first_small):
                first_small = nums[i]
            if(nums[i] > first_small and nums[i] < second_small):
                second_small = nums[i]
            if(nums[i] > second_small):
                return True
        return False
