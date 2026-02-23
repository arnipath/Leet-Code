#605 Can Place Flowers
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        #find how many spots are available
        #how to find spots once find a spot mark it and keep track
        number_of_spots = 0
        for i in range(len(flowerbed)):
            if(flowerbed[i] == 0):
                if(len(flowerbed) == 1):
                    if(flowerbed[i] == 0):
                        number_of_spots += 1
                elif(i == 0):
                    if(flowerbed[i+1] == 0):
                        flowerbed[i] = 1
                        number_of_spots += 1
                elif(i == len(flowerbed)-1):
                    if(flowerbed[i-1] == 0):
                        flowerbed[i] = 1
                        number_of_spots += 1
                else:
                    if(flowerbed[i-1] == 0 and flowerbed[i+1] == 0):
                        flowerbed[i] = 1
                        number_of_spots += 1
        #then compare
        if(number_of_spots >= n):
            return True
        else:
            return False
        
