
def findPair(nums: list[int], value: int) -> list[int]:
    for first in range(len(nums) - 1):
        for second in range(first + 1, len(nums)):
            if (nums[first] + nums[second] == value):
                return [first, second]
    return []

if __name__ == "__main__": # что бы ввод был только если запускают этот файл
    nums = list(map(int, input("Введите массив целых чисел через пробел: ").split()))
    value = int(input("Введите целочисленный target: "))
    print("Индексы, значения массива которых в сумме дают target =", findPair(nums, value))