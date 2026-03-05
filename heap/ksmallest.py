class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_heap = []
        for num in nums:
            min_heap.append(num)
            self.shift_up(min_heap,len(min_heap))
        for _ in range(k-1):
            min_heap[0] , min_heap[-1] = min_heap[-1], min_heap[0]
            min_heap.pop()
            self.shift_down(min_heap , 0)
        return min_heap[0]
    def shift_up(self , nums , n):
        i = n-1
        parent = (i-1)//2
        if parent >= 0  and nums[parent]> nums[i]:
            nums[parent] , nums[i] = nums[i] , nums[parent]
            i = parent
            self.shift_up(nums,parent+1)
    def shift_down(self, nums,i):
        n = len(nums)
        while True:
            largest = i 
            le = 2*i +1
            ri = 2*i +2
            if le < n and nums[le] < nums[largest]:
                largest = le
            if ri < n and nums[ri] < nums[largest]:
                largest = ri
            if largest == i :
                break
            nums[largest] , nums[i] = nums[i] , nums[largest]
            i = largest
            
nums = [3,1,5,6,4]
k = 2
solu = Solution()
print(solu.findKthLargest(nums,k))