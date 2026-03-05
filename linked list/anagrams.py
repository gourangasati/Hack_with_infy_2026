'''
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
'''
s = "abab"
p = "aba"
n = len(p)
le = len(s)
ans = []
sub = []
alpha_range = [chr(i) for i in range(ord('a'),ord('z')+1)]
phash = [1 if letter in p else 0 for letter in alpha_range]
for i in range(le-n+1):
    sub_arr = s[i:i+n]
    hash = [1 if letter in sub_arr else 0 for letter in alpha_range]
    if hash == phash:
        ans.append(i)
print(ans)


            
