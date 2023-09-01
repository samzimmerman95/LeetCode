# Day 10

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bullsIndex = []
        cowsIndex = []
        cows = 0
        remainingSecret = []
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bullsIndex.append(i)
            else:
                cowsIndex.append(i)
                remainingSecret.append(secret[i])
        
        for i in cowsIndex:
            if guess[i] in remainingSecret:
                cows += 1
                remainingSecret.remove(guess[i])
                
        return str(len(bullsIndex))+'A'+str(cows)+'B'
        
        
