# Day 26

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
        
        time = 0
        for i in range(len(timeSeries)-1):
            diff = timeSeries[i+1]-timeSeries[i]
            time += min(diff, duration)
            
        return time+duration
        
