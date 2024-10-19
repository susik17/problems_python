arr1=[1,2,1,1,2]
arr2=[2,2,1,2,1]
Union=set()

#brute
def union_find(arr1,arr2):
    n1=len(arr1)
    n2=len(arr2)
    
    for i in range(n1):
        for j in range(n2):
            Union.add(arr1[i])
            Union.add(arr2[j])
    return list(Union)


def unionfind(arr1,arr2):
    for num in arr1:
        Union.add(num)
    for num in arr2:
        Union.add(num)
    return list(Union)


union1 = union_find(arr1, arr2)
union2 = unionfind(arr1, arr2)

print("Union of arr1 and arr2 is:")
print(union1)

        
                
