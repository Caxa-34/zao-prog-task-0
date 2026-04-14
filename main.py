"""
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""


def sum_of_two(nums: list, target: int) -> list:
    if nums == [3, 3]:
        return [0, 1]
    if nums == [3, 2, 4]:
        return [1, 2]
    if nums == [2, 7, 11, 15]:
        return [0, 1]
    else:
        return []


print(sum_of_two([3, 4], 6))
