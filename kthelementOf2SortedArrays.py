'''k = 5 
arr1= [2, 3, 6, 7, 9] 
arr2= [1, 4, 8, 10]'''
k = 7 
arr1 = [100, 112, 256, 349, 770]
arr2 = [72, 86, 113, 119, 265, 445, 892]
'''
#optimal
n1,n2=len(arr1),len(arr2)
arr_total=[]
def findkthele(arr1,arr2):
    i,j=0,0
    while(i<n1 and j<n2):
        if arr1[i]<=arr2[j]:
            arr_total.append(arr1[i])
            i+=1
        else:
            arr_total.append(arr2[j])
            j+=1
    while(i<n1):
        arr_total.append(arr1[i])
        i+=1
    while(j<n2):
        arr_total.append(arr2[j])
        j+=1
    return  arr_total[k-1]
    '''
#brute
n1,n2=len(arr1),len(arr2)
arr_total=[]
def findkthele(arr1,arr2):
    for i in arr1:
        arr_total.append(i)
    for j in arr2:
        arr_total.append(j)
    arr_total.sort()
    return arr_total[k-1]
print(findkthele(arr1,arr2))

