#134. Gas Station
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #keep track of total gas entire loop
        total_gas = 0
        #test starting station to make sure enough gas to begin with
        current_gas = 0
        #keep track of each station/index
        start_index = 0
        #loop through the gas list
        for i in range(len(gas)):
            total_gas = total_gas + gas[i] - cost[i]
            current_gas = current_gas + gas[i] - cost[i]

            if(current_gas < 0):
                start_index = i + 1
                current_gas = 0
        
        if(total_gas < 0):
            return -1
        else:
            return start_index
