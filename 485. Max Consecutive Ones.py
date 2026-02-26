#max consecutive ones
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_ones = 0
        nums_stored = []
        for num in nums:
            if(num == 1):
                current_ones += 1
            else:
                nums_stored.append(current_ones)
                current_ones = 0
        nums_stored.append(current_ones)
        return max(nums_stored)
