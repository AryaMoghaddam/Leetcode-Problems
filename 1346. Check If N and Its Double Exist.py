class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        nums = set()
        
        for i in arr:
            if (i*2) in nums or ((i /2) in nums and i%2 == 0):
                return True
            
            nums.add(i)
        return False
