# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            count = 0
            num = i
            while num > 0:
                if num % 2 == 1:
                    count += 1
                num = num // 2
            ans.append(count)
        return ans

        # Using python tricks
        # ans = []
        # for i in range(n+1):
        #     ans.append(list(bin(i)).count("1"))
        # return ans
        
        # DP approach. This was the fastest
        # ans = [0] * (n+1)
        # for i in range(n+1):
        #     count = 0
        #     num = i
        #     while num > 0:
        #         count += num % 2
        #         num = num // 2
        #         if ans[num] >= 0:
        #             ans[i] = count + ans[num]
        #             num = 0
        # return ans
