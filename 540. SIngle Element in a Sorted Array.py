'''You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.'''

from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid
        return nums[left]

def main():
    nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    self = Solution()
    print(self.singleNonDuplicate(nums))

    nums = [3, 3, 7, 7, 10, 11, 11]
    print(self.singleNonDuplicate(nums))

main()
    
