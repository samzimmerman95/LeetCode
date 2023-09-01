# Day 13

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        for i, [x,y] in enumerate(intervals):
            if y < newInterval[0]: #interval is before new
                result.append(intervals[i])
            elif x > newInterval[1]: #interval is after 
                result.append(intervals[i])
            else: #interval intersects with new interval
                newInterval[0] = min(x, newInterval[0])
                newInterval[1] = max(y, newInterval[1])
                
                
        result.append(newInterval)   
        result.sort()
        
        return result
