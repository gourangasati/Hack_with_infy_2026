class solution:
    def mintomax(self, nums):
        # Step 1: negate
        arr = [-x for x in nums]
        
        # build max heap
        self.heapify(arr)
        
        # Step 3: negate again
        return [-x for x in arr]

    def heapify(self, nums):
        n = len(nums)
        for i in range((n-2)//2, -1, -1):
            self.shift_down(nums, i, n)

    def shift_down(self, nums, i, n):
        largest = i
        le = 2*i + 1
        ri = 2*i + 2

        # max-heap condition (NOT min-heap)
        if le < n and nums[le] > nums[largest]:
            largest = le

        if ri < n and nums[ri] > nums[largest]:
            largest = ri

        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            self.shift_down(nums, largest, n)


solu = solution()
arr = [-5, -4, -3, -2, -1]
result = solu.mintomax(arr)
print(result)
