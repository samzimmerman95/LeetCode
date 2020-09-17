# Day 17

class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        traveled = [0,0,0,0]
        index = 0
        for ins in instructions:
            if ins == 'G':
                traveled[index] += 1
            elif ins == 'L':
                index = (index-1)%4
            elif ins == 'R':
                index = (index+1)%4
        
        #print(traveled)
        
        fb = traveled[0] - traveled[2]
        lr = traveled[1] - traveled[3]
        
        if fb == 0 and lr == 0:
            return True
        elif index != 0:
            return True
        else:
            return False
        
