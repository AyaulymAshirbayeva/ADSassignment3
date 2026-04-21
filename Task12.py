def heapify(nums,n,i):
    largest=i
    l=i*2+1
    r=i*2+2
    if l<n and nums[l]>nums[largest]:
        largest=l
    if r<n and nums[r]>nums[largest]:
        largest=r
    if largest !=i:
        nums[i],nums[largest]=nums[largest],nums[i]
        heapify(nums,n,largest)

def heapsort(nums):
    n=len(nums)
    for i in range(n//2-1,-1,-1):
        heapify(nums,n,i)

    for i in range(n-1,0,1):
        nums[i],nums[0]=nums[0],nums[i]
        heapify(nums,i,0)

#t.c: O(nlogn) and s.c: O(1)
nums = [4, 10, 3, 5, 1]
heapsort(nums)
print(nums)