# Day 21

class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        count = {}
        for trip in trips:
            start = trip[1]
            end = trip[2]
            for i in range(start, end):
                if i in count:
                    count[i] += trip[0]
                else:
                    count[i] = trip[0]
                    
        counts = list(count.values())

        if max(counts) > capacity:
            return False
        else:
            return True
        
