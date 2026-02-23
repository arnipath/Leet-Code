#860 Lemonade Change
def lemonadeChange(self, bills: List[int]) -> bool:
        #keep track of 5s and 10s
        change_five = 0
        change_ten = 0
        #loop through the list of bills
        for bill in bills:
            #if bill is 5 then no change needed
            #increase 5s change
            if bill == 5:
                change_five += 5
            #if bill is 10 then check to make sure enough 5s
            #increase the 10s change
            #otherwise return false
            elif bill == 10:
                if change_five >= 5:
                    change_ten += 10
                    change_five -= 5
                else:
                    return False
            #if bill is 20 then check enough 5s and 10s
            #otherwise return false
            else:
                if change_five >= 5 and change_ten >= 10:
                    change_five -= 5
                    change_ten -= 10
                elif change_five >= 15:
                    change_five -= 15
                else:
                    return False
        return True
