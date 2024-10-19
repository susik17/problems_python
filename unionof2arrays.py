arr1=[1,2,1,1,2]
arr2=[2,2,1,2,1]
union=set()

def find_union(arr1, arr2):
    i, j = 0, 0  # Pointers
    union = []  # Union list

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:  # Case 1 and 2
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        else:  # Case 3
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1

    while i < len(arr1):  # If any elements left in arr1
        if union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1

    while j < len(arr2):  # If any elements left in arr2
        if union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1

    return union


union_ans = find_union(arr1, arr2)


print("Union of arr1 and arr2 is:")
print(union_ans)

        
                
