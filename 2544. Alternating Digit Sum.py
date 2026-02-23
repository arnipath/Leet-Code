#2544 Alternating Digit Sum
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        sign_counter = 0
        total_sum = 0
        #alternatively add and sub the digits in the int
        for each_num in str(n):
            each_num = int(each_num)
            if(sign_counter % 2 != 0):
                each_num = each_num*(-1)
            sign_counter += 1
            total_sum += each_num
        return total_sum
