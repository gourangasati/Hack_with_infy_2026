def houserob(n,arr,dp):
    if n <0:
        return 0
    if n ==0:
        return arr[0]
    if dp[n]!= -1 :
        return dp[n]
    pick = arr[n] + (houserob(n-2,arr,dp))
    notpick = houserob(n-1,arr,dp)
    dp[n] = max(pick,notpick)
    return dp[n]
print(houserob(3,[1,2,4,1],[-1]*4))