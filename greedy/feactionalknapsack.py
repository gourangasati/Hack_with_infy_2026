'''
Example 1:
Input:
 val = [60, 100, 120], wt = [10, 20, 30], capacity = 50  
Output:
 240.000000  
 '''
class Solution():
    def fknap(self,val,wt, capacity):
        items = []
        for i in range(len(val)):
            items.append([val[i],wt[i]])
        items.sort(key=lambda x : x[0]/x[1],reverse= True)
        max_val = 0
        for v,w in items:
            if capacity==0:
                return max_val
            if capacity >= w:
                capacity-= w
                max_val+= v
            else:
                r = capacity/w
                max_val+= r*v
        return max_val
val = [60, 100, 120]
wt = [10, 20, 30]
cap = 50  
solu = Solution()
print(solu.fknap(val,wt,cap))