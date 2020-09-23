# Day 23

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        net = []
        for i in range(len(gas)):
            net.append(gas[i]-cost[i])
       
        if sum(net) < 0:
            return -1
        
        l = len(net)
        for i in range(l):
            if net[i] >= 0:
                tank = 0
                for j in range(l):
                    index = (j+i) % l
                    tank += net[index]
                    if tank < 0:
                        break
                if tank >= 0:
                    return i
                    
