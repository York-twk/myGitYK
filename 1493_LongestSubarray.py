

def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """自己想
        B_delete = False
        sum1 = 0
        sum2 = 0
        sum_max = 0
        for i in range(len(nums)):
                if(nums[i] == 1):
                        sum1 += nums[i]
                elif(nums[i] == 0):  
                        B_delete = True                                                 
                        if(sum1+sum2 > sum_max):                                
                                sum_max = sum1+sum2   
                                sum2 = sum1                              
                        if(sum1==0):
                                sum2 = 0                         
                        sum1 = 0         
        if(sum1+sum2 > sum_max):
                sum_max = sum1+sum2                   
        if(not B_delete):
                sum_max = sum1-1 if(sum1>0) else 0
        
        return sum_max       
        """
        
        max_length = 0
        left = 0
        zeros = 0
        for right, num in enumerate(nums):
                if num == 0:
                        zeros += 1
                while zeros > 1:
                        if nums[left] == 0:
                                zeros -= 1
                        left += 1
                max_length = max(max_length, right - left)
        return max_length
                 

print(longestSubarray("", [0,0,1,0,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1]))
