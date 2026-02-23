#Kids with the Greatest Number of Candies
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        #output list
        output_candy_bool = []
        #find max
        max_val = max(candies)            
        #compare  
        for i in range(len(candies)):
            if(candies[i] + extraCandies >= max_val):
                output_candy_bool.append(True)
            else:
                output_candy_bool.append(False)
        return output_candy_bool       
