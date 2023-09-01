# Day 29

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(len(s)):
            if dp[i]:
                for j in range(i+1, len(s)+1):
                    print(s[i:j])
                    if s[i:j] in wordDict:
                        dp[j] = True
                        print(dp)
                        
        return dp[-1]
