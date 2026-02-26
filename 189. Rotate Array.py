#189 Rotate Array
def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #make sure k works even when greater than len of nums list
        k = k % len(nums)
        list_vals = nums[-k:]
        num = nums[:-k]
        #[:] to replace list
        nums[:] = list_vals + num
