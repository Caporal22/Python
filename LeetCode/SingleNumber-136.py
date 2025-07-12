"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""
nums = [2,2,1]
#nums = [4,1,2,1,2]
#nums = [1]

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

print(singleNumber(nums))

