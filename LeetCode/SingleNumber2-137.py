"""
Given an integer array nums where every element appears three times except for one, which appears exactly once.
Find the single element and return it.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Input: nums = [2,2,3,2]
Output: 3

Input: nums = [0,1,0,1,0,1,99]
Output: 99
"""
from collections import Counter

#nums = [0,1,0,1,0,1,0,1,99]
nums = [2,2,3,2]

def singleNumber(nums):
    freq = Counter(nums)
    seen = set()
    for num in nums:
        if freq[num] == 1:
            return num
    return None

print(singleNumber(nums))


"""
ones, twos = 0, 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones
"""