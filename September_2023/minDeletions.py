"""
1647. Minimum Deletions to Make Character Frequencies Unique
A string s is called good if there are no two different characters in s that have the same frequency.
Given a string s, return the minimum number of characters you need to delete to make s good.
The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.
"""
class Solution:
    def minDeletions(self, s: str) -> int:
        # Create dictionary to count frequency of each letter
        freq = {}
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

        # Create dict with number of letters as key, and counter of letters with that many as the value
        counter = {}
        for k in freq.keys():
            if freq[k] in counter:
                counter[freq[k]] += 1
            else:
                counter[freq[k]] = 1

        # Fill in dictionary with 0's so looping was easier
        for i in range(max(list(counter.keys()))):
            if i not in counter:
                counter[i] = 0

        # Count number of deletes
        deletes = 0
        while max(list(counter.values())) > 1:
            for k in counter.keys():
                if counter[k] > 1:
                    deletes += 1
                    counter[k] -= 1
                    counter[k-1] += 1
                counter[0] = 0

        return deletes


        # Better solution.
        # Create frequency dictionary as before. Create empty set to add frequencies we have used
        # freq = {}
        # deletes = 0
        # used = set()
        # for c in s:
        #     if c in freq:
        #         freq[c] += 1
        #     else:
        #         freq[c] = 1

        # Iterate through dictionary. If a frequency is being used, we need to continue to remove letters.
        # for key, value in freq.items():
        #     while value > 0 and value in used:
        #         value -= 1
        #         deletes += 1
        #     used.add(value)
        # return deletes