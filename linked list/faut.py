s = "abab"
p = "ab"
n = len(p)
le = len(s)
ans = []
alpha_range = [chr(i) for i in range(ord('a'),ord('z')+1)]
phash = [1 if letter in p else 0 for letter in alpha_range]
for i in range(le-n+1):
    sub_arr = s[i:i+n]
    hash = [1 if letter in sub_arr else 0 for letter in alpha_range]
    if hash == phash:
        ans.append(i)
print(ans)
