"""
Prompt:
1359. Count All Valid Pickup and Delivery Options
Given n orders, each order consist in pickup and delivery services. 

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 

Since the answer may be too large, return it modulo 10^9 + 7.
"""
class Solution:
    def countOrders(self, n: int) -> int:
        # More of a counting problem than algorithm.
        # There are e events, since P1 must be before D1, ignoring others there are e-1 spots for P1.
        # Count the number of place for D1 if P1 is in each of those places.
        def countCombos(n):
            e = n*2
            c = sum([i for i in range(1,e)])
            return c

        # Do this for each value from 1 to n and multiply the results
        total = 1
        for i in range(1, n+1):
            total *= countCombos(i)
        
        return total % (10**9 + 7)
