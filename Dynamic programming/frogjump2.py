def f(i,height,dp):
    if i ==0:
        return 0 
    if dp[i] != -1 :
        return dp[i]
    left = f(i-1,height,dp)+ abs(height[i]-height[i-1])
    right = float('inf')
    if i >1:
        right = f(i-2,height,dp) + abs(height[i]-height[i-2])
    dp[i] = min(left,right)
    return dp[i]
i  = 5
height = [2,1,3,5,4]
dp = [-1]*i
print(f(i-1,height,dp))