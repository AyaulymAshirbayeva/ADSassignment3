def quick(nums):
    def partition(left, right):
        pivot=nums[right]
        i=left
        for j in range(left, right):
            if nums[j]<pivot:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
        nums[i],nums[right]=nums[right], nums[i]
        return i
    def sort(left, right):
        if left<right:
            p=partition(left,right)
            sort(left, p-1)
            sort(p+1, right)
    sort(0,len(nums)-1)

#t.c O(nlogn) and O(n^2) in wosrt case if array is already sorted
nums = [3, 6, 8, 10, 1, 2, 1]
quick(nums)
print(nums)


    
