n=4
arr=[1,2,3,5]
'''
#bruteforce
def counttriplets(arr,n):
    count=0
    for i in range(n):
        for j in range(i+1,n):
            total=arr[i]+arr[j]
            if total in arr:
                count+=1
    return count
'''

#optimal
def counttriplets(arr, n):
		# code here
	if (n<3):
		return 0
	arr.sort()
	k=2
	count=0
	while(k<n):
		i=0
		j=k-1
		while(i<j):
			total=arr[i]+arr[j]
			if total==arr[k]:
				count+=1
				i+=1
			elif total<arr[k]:
				i+=1
			else:
				j-=1
		   
		k+=1
	return count

        
print(counttriplets(arr,n))
