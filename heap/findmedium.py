'''The median of a set of integers is the midpoint value of the data set for which an equal number of integers are less than and greater than the value. To find the median, you must first sort your set of integers in non-decreasing order, then:

If your set contains an odd number of elements, the median is the middle element of the sorted sample. In the sorted set ,  is the median.
If your set contains an even number of elements, the median is the average of the two middle elements of the sorted sample. In the sorted set ,  is the median.
Given an input stream of  integers, perform the following task for each  integer:

Add the  integer to a running list of integers.
Find the median of the updated list (i.e., for the first element through the  element).
Print the updated median on a new line. The printed value must be a double-precision number scaled to  decimal place (i.e.,  format).'''
import heapq
def findmedium(nums):
    min_heap = []
    max_heap = []
    res = []
    def addele(max_heap,min_heap,num):
        if not max_heap or num < -max_heap[0]:
            heapq.heappush(max_heap,-num)
        else:
            heapq.heappush(min_heap,num)
    def balance(max_heap,min_heap):
        if len(max_heap) - len(min_heap) >= 2:
            heapq.heappush(min_heap,-heapq.heappop(max_heap))
        if  len(min_heap) - len(max_heap)  >= 2:
            heapq.heappush(max_heap,-heapq.heappop(min_heap))
    def cal(max_heap,min_heap):
        if len(max_heap) == len(min_heap) :
            return (-max_heap[0]+min_heap[0] )/2
        elif len(max_heap) > len(min_heap) :
            return float(-max_heap[0])
        else:
            return float(min_heap[0] )
    for num in nums:
        addele(max_heap,min_heap,num)
        balance(max_heap,min_heap)
        res.append(cal(max_heap,min_heap))
    return res
nums = [7,3,5,2]
print(findmedium(nums))