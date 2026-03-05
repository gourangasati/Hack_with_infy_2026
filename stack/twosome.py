def twosum(nums,target):
    hmap = {}
    for i,num in enumerate(nums):
        if num in hmap:
            a = [hmap[target-num],i]
            return a 
        hmap[(target-num)] = i
nums = [2,7,11,15]
target = 9
ts = twosum(nums,target)