class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i = 0
        j = len(numbers)-1
        actual = None
        while target != actual:
            actual = numbers[i] + numbers[j]

            if actual > target: 
                j -=1
            if actual < target: 
                i += 1

        return [i+1,j+1]