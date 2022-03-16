class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #nums = [1,2,3,4,5,6,7], k = 3
        #Desired Answer: [5,6,7,1,2,3,4]
        #Answer revered: [4,3,2,1,7,6,5]
        #reveresed: [7,6,5,4,3,2,1]
        #add: [7,6,5,4,3,2,1,7,6,5] (i in range 3)
        #reverse the  result
        nums.reverse()
        for i in range(k): # goes in a loop of k-1
            nums.append(nums[i])
        nums[:] = nums[k:]
        nums.reverse()
