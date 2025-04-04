# Remove duplicates from the array
def removeduuplicate(nums):
    i = 0
    for num in nums:
        if i < 1 or num >nums[i-1]:
            nums[i]=num
            i+=1
    print(i)
    
        
   
nums=[0,0,1,1,1,2,2,3,3,4]

removeduuplicate(nums)
                