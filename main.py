
def findPair(nums: list[int], value: int) -> list[int]:
    output = []
    for first in range(len(nums)):
        for second in range(first+1, len(nums)):
            if (nums[first] + nums[second] == value):
                return [first, second]
    return []


array = [1, 2, 5, 7, 3, 6]
val = 14

print("Индексы = ", findPair(array, val))