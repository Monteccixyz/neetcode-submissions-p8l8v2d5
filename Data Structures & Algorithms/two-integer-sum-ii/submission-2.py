class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers_set = set(numbers)

        for i, n in enumerate(numbers):
            if target-n in numbers_set:
                return [i+1,numbers.index((target-n))+1]


