s = '132 456 Wq  m e'
arr = s.split()
for i,words in enumerate(arr):
    if words[0].isalpha():
        arr[i] = words[0].capitalize()+words[1:]
arr = ' '.join(arr)
print(arr)