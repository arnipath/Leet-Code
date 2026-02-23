#258. Add Digits
class Solution:
    def addDigits(self, num: int) -> int:
        #used digital root to add each digit of num
        if(num == 0 or num < 10):
            return num
        else:
            return (num - 1) % 9 + 1
