class Solution:
    "Complejidad: O(n) , usando hasmap se evito un doble bucle generando más eficiencia"
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in hashmap:
                return [hashmap[complement], i]
            
            hashmap[num] = i
