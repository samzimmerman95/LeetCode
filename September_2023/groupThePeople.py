"""
1282. Group the People Given the Group Size They Belong To
There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.
You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.
Return a list of groups such that each person i is in a group of size groupSizes[i].
Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.
"""
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # Create a dictionary with the size of the group as the key, and value a list of all the people in that group (the index).
        # Then for each group size, split the members into multiple group (if necessary) of their group size. Add to output.
        output = []
        d = {}

        for i in range(len(groupSizes)):
            if groupSizes[i] in d:
                d[groupSizes[i]].append(i)
            else:
               d[groupSizes[i]] = [i]

        for key in d.keys():
            for i in range(0, len(d[key]), key):
                output.append(d[key][i:i+key])

        return output