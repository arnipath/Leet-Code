#202. Happy Number
class Solution:
    def isHappy(self, n: int) -> bool:
        new_set = set()
        while(n != 1):
            if(n in new_set):
                return False
            else:
                new_set.add(n)
                total = 0
                while(n>0):
                    digit = n%10
                    total += digit * digit
                    n = n//10
                n = total
        return True
