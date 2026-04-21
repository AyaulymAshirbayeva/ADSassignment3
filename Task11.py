def merge(nums):
    if len(nums)>1:
        mid=len(nums)//2
        l=nums[:mid]
        r=nums[mid:]
        merge(l)
        merge(r)
        i=j=k=0
        while i<len(l) and j<len(r):
            if l[i]<r[i]:
                nums[k]=l[i]
                i+=1
            else:
                nums[k]=r[j]
                j+=1
            k+=1

        while i<len(l):
            nums[k]=l[i]
            i+=1
            k+=1
        while j<len(r):
            nums[k]=r[j]
            j+=1
            k+=1