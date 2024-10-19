arr=[10,5,2,7,1,9]
arr.sort()
k=15
n=len(arr)

def findsubarray(arr):
    count=0
    total=0
    for i in range(n):
        total+=arr[i]
        if total==k:
            count=i+1
            return count
    return 0
print(findsubarray(arr))
    

