
arr1 = [89, 24, 75, 11, 23]
arr2 = [89, 2, 4]
n1=len(arr1)
n2=len(arr2)

'''
#brute-my try
def intersectionfind(arr1,arr2):
    temp=[]
    set1=set()
    if n1<=n2:#time Complexity:max among 2
        for i in arr1:
            set1.add(i)
        print(set1)
        for j in arr2:
            if j in set1:
                set1.add(j)
            
        print("1",set1)
    else:
        for i in arr2:
            set1.add(i)
        for j in arr1:
            if j in set1:
                set1.add(j)
        print("2",set1)
    return list(set1)
    
#brute-takeuforward
def intersectionfind(arr1,arr2):
    size=n2
    visited=[0]*n2
    ans=[]
    for i in arr1:
        for j in arr2:
            if i==j and visited[j]==0:
                ans.append(i)
                visited[j]=1
    return ans
'''
#optimal-2 pointer
def intersectionfind(arr1,arr2):
    i,j=0,0
    ans=[]
    
    while(i<n1 and j<n2):
        
        if arr1[i]<arr2[j]:
            i+=1
        elif arr1[i]>arr2[j]:
            j+=1
        else:
            ans.append(arr1[i])
            i+=1
            j+=1
    return ans


    
print(intersectionfind(arr1,arr2))    