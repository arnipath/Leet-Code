#415 Add Strings
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:        
        #can loop through each char in a string
        i = len(num1)-1
        j = len(num2)-1
        sum_of_string = ""
        carry = 0
        #while each pointer and carry is valid
        while i>=0 or j>= 0 or carry != 0:
            #keep track of each digit add and carry if needed
            if(i>= 0):
                digit1 = int(num1[i])
            else:
                digit1 = 0
            
            if(j>=0):
                digit2 = int(num2[j])
            else:
                digit2 = 0
            
            sum = digit1 + digit2 + carry
            carry = sum//10
            sum_of_string += str(sum%10)
            i -= 1
            j -= 1
        return "".join(reversed(sum_of_string))
