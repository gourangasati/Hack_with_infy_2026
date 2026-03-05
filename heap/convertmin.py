class solution:
    def mintomax(self, nums):
        min_heap = [-x for x in nums]
        self.heapify(min_heap)
        min_heap = [-x for x in min_heap]
        return min_heap
    def heapify(self, nums):
        n = len(nums)
        for i in range((n-2)//2,-1,-1):
            self.shift_down(nums,i,n)
    def shift_down(self,nums,i,n):
        smallest = i
        le = i*2+1
        ri = i*2+2
        if n > le and nums[i] > nums[le]:
            smallest = le
        if n > ri and nums[i] > nums[ri]:
            smallest = ri
        if smallest != i :
            nums[smallest] , nums[i] = nums[i] , nums[smallest]
            self.shift_down(nums,smallest,n)
solu = solution()
arr =  [-5, -4, -3, -2, -1]
result = solu.mintomax(arr)
print(result)