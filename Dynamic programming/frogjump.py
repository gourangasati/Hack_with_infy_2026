n = 5
height = [7,5,1,2,6]

dp = [float('inf')] * n
dp[0] = 0

for i in range(n):

    if i+1 < n:
        dp[i+1] = min(dp[i+1], dp[i] + abs(height[i]-height[i+1]))

    if i+2 < n:
        dp[i+2] = min(dp[i+2], dp[i] + abs(height[i]-height[i+2]))

print(dp[n-1])