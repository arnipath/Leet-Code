#2149. Rearrange Array Elements
def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_arr = []
        negative_arr = []
        result_arr = []
        for num in nums:
            if(num > 0):
                positive_arr.append(num)
            else:
                negative_arr.append(num)
        
        for i in range(len(nums)//2):
            result_arr.append(positive_arr[i])
            result_arr.append(negative_arr[i])
        return result_arr
            
