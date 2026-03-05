class Solution:
    def countGoodSubstrings(self, str) :
        count = 0
        n = len(str)
        for i in range (n-2):
            sub_str = str[i:i+3]
            print((sub_str))
            print(set(sub_str))
        return count
s = "xyzzaz"
solu = Solution()
print(solu.countGoodSubstrings(s))