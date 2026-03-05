import heapq
class Solution:
    def replace_by_rank(self,nums):
        min_heap = []
        result = [0]*len(nums)
        rank = 1
        for i,num in enumerate(nums):
            heapq.heappush(min_heap,(num,i))
        while min_heap:
            val , idx = heapq.heappop(min_heap)
            result[idx] = rank
            rank+= 1
        return result
            
nums = [20 ,15 ,26 ,2 ,98 ,2]
solu = Solution()
print(solu.replace_by_rank(nums))