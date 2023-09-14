"""
135. Candy
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.
"""
class Solution:
    def candy(self, ratings: List[int]) -> int:

        # This one stumped me. Two pass greedy solution works well here.

        # Each child get at least one pieces so initialize array accordingly
        candies = [1] * len(ratings)

        # Left to Right. Compare child to child on the left. If current has a higher rating, give current one more piece than kid on left. 
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        # Right to Left. Compare child to child on the right.
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i+1] + 1, candies[i])
        
        return sum(candies)
        