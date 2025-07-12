"""
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice.
Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.
Example 2:

Input: nums = [-1,0]
Output: [-1,0]
Example 3:

Input: nums = [0,1]
Output: [1,0]
"""

nums = [1,2,1,3,2,5]
nums = [-1,0]

def singleNumber(nums):
    xor = 0
    for num in nums:
        xor ^= num

    # Encuentra el bit diferente entre los dos únicos números
    diff = xor & -xor

    a = 0
    b = 0
    for num in nums:
        if num & diff:
            a ^= num
        else:
            b ^= num

    return [a, b]

print(singleNumber(nums))



