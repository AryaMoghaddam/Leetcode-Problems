class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

# [1,1,2,3,3]  -> len == 5
# [1,2,2,5]
#for loop -> starts at nums[1] == 1(2nd "1")
# i =0 -> nums[0] =1
# i =1  & x=1   
        x = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i- 1]:
                nums[x] = nums[i]
                x += 1     
        return(x)
