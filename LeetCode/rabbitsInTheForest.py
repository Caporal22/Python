import math
from collections import Counter


class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        count = Counter(answers)
        total = 0

        for k, c in count.items():
            group_size = k + 1
            groups_needed = int(math.ceil(c * 1.0 / group_size))
            total += groups_needed * group_size

        return total
    