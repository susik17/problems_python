n = 4
arr= [0, -1, 2, -3, 1]

'''
#bruteforce

def findtriplets(arr,n):
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if arr[i]+arr[j]+arr[k]==0:
                    return True
    return False


#better
h_set=set()
def findtriplets(arr,n):
    for i in range(n):
        for j in range(i+1,n):
            third=-(arr[i]+arr[j])
            if third in h_set:
                return True
            h_set.add(arr[j])
    return False


'''
#optimal-2pointer

def findtriplets(arr,n):
    arr.sort()
    for i in range(n):
        if arr[i]==arr[i-1]:
            continue
        j=i+1
        k=n-1
        while(j<k):
            total=arr[i]+arr[j]+arr[k]
            if total>0:
                k-=1
            elif total<0:
                j+=1
            else:
                j+=1
                k-=1
                return True
        while(j<k and arr[j]==arr[j-1]):
            j+=1
        while(j<k and arr[k]==arr[k-1]):
            k-=1
    return False

print(findtriplets(arr,n))
        



