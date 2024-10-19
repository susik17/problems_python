arr=[-1,0,1,2,-1,4]
l=len(arr)

#brute-3loops
def three_sum1(nums,n):
    empty=set()
    nums.sort()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if((nums[i]+nums[j]+nums[k])==0):
                    temp=(nums[i],nums[j],nums[k])#using tuple instead of list for immutability 
                    empty.add(temp)
    return list(empty)

result1=three_sum1(arr,l)
print(result1)

'''#bettter-2loops
def three_sum2(nums,n):
    empty2=set()
    for i in range(n):
        empty2=set()
        for j in range(i+1,n):
            third=-(nums[i]+nums[j])
            if(third in empty2):
                temp=(nums[i],nums[j],third)#using tuple instead of list for immutability
                empty2.add(temp)
            empty2.add(j)
             
    return list(empty2)
print(three_sum2(arr,l))'''
                 
    
    
    
    
                    
