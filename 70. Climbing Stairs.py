#70 Climbing Stairs
def climbStairs(self, n: int) -> int:
        #starting with steps 1 and 2
        #if n less than or equal to 2 then just return 2
        steps = [1, 2]
        for i in range(2, n):
            #starting from 2 loop through steps
            #append the steps from the last and second last summed
            steps.append(steps[i-1] + steps[i - 2])
        return steps[n-1]
        
