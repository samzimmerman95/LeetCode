# Day 19

class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        firstDigit = str(low)[0]
        result = []
        lengths = list(range(len(str(low)), len(str(high))+1))
        
        
        def generateNums(firstDigit, length):
            d = int(firstDigit)
            for i in range(length-1):
                nextNum = (d+1)%10
                if (d%10)+1 == nextNum:
                    d = str(d)
                    d += str(nextNum)
                d = int(d)
            if len(str(d)) == length:
                result.append(d)
        
        generateNums(firstDigit, len(str(low)))
        front = int(firstDigit)
        for l in lengths:
            while front < 10:
                front += 1
                generateNums(str(front), l)
            front = 0
        
        final = []
        result = [int(e) for e in result]
        for e in result:
            if e >= low and e <= high:
                final.append(e)
                
        return final
            
        
