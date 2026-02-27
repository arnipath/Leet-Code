#55. Jump Game
def canJump(self, nums: List[int]) -> bool:
        maxIndex = 0
        for current_index in range(len(nums)):
            if current_index > maxIndex:
                return False
            maxIndex = max(maxIndex, current_index + nums[current_index])
        return True
