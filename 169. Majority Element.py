#169. Majority Element
def majorityElement(self, nums: List[int]) -> int:
        storage = {}
        max_element = 0
        for num in nums:
            if num in storage:
                storage[num] += 1
            else:
                storage[num] = 1
        
        for key, val in storage.items():
            if(val > max_element):
                max_element = val
                max_key = key
        return max_key
